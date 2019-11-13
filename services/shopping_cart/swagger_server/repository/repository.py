import os
import contextlib
from typing import List

import sqlalchemy
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker, lazyload
from sqlalchemy_utils import database_exists, create_database

from swagger_server.models import article as domain
from swagger_server.repository import entities
from swagger_server.exceptions.exceptions import *

db_username = 'postgres'
db_password = 'NotMyBestIdea'
if 'DB' in os.environ:
    db_host = os.environ['DB']
else:
    db_host = 'localhost'
db_port = 5432
db_db = 'shopping_cart'

db_string = f"postgres+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_db}"

engine = sqlalchemy.create_engine(db_string)

if not database_exists(engine.url):
    create_database(engine.url)

# entities.Base.metadata.drop_all(engine)
# entities.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# @contextlib.contextmanager
# def get_session():
#     with contextlib.closing(Session()) as session:
#         yield session


class Repository:
    session: Session

    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.flush()
        self.session.close()

    def create_cart(self, user_id: int) -> int:
        if not self.user_exists(user_id):
            cart = entities.Cart()
            cart.user_id = user_id
            self.session.add(cart)
            self.session.commit()
            return cart.id
        else:
            self.session.query(entities.Cart) \
                .filter(entities.Cart.user_id == user_id) \
                .one_or_none()

    def get_cart(self, user_id: int) -> entities.Cart:
        return self.session.query(entities.Cart) \
            .options(lazyload('items')) \
            .filter(entities.Cart.user_id == user_id) \
            .one_or_none()

    def delete_cart(self, user_id: int):
        if not self.user_exists(user_id):
            raise NotFoundException()
        self.session.query(entities.Cart) \
            .filter(entities.Cart.user_id == user_id) \
            .delete()
        self.session.commit()

    def get_items(self, user_id: int) -> List[domain.Article]:
        cart = self.get_cart(user_id)
        if cart is None:
            raise NotFoundException()
        return [a.to_domain() for a in cart.items]

    def add_item(self, cart_id: int, article: domain.Article):
        article_entity = self.get_article(cart_id, article.article_id)
        if article_entity is not None:
            article_entity.quantity += article.quantity
        else:
            article_entity = entities.Item()
            article_entity.article_id = article.article_id
            article_entity.quantity = article.quantity
            article_entity.cart_id = cart_id
            self.session.add(article_entity)

        self.session.commit()

    def remove_item(self, user_id: int, article_id: int):
        if not self.user_exists(user_id):
            raise NotFoundException()
        cart = self.get_cart(user_id)
        self.session.query(entities.Item) \
            .options(lazyload('cart')) \
            .filter(entities.Item.cart_id == cart.id) \
            .filter(entities.Item.article_id == article_id) \
            .delete()
        self.session.commit()

    def checkout_cart(self, cart_id: int) -> List[domain.Article]:
        articles = self.get_items(cart_id)
        self.session.query(entities.Item) \
            .filter(entities.Item.cart_id == cart_id) \
            .delete()
        self.delete_cart(cart_id)
        return articles

    def user_exists(self, user_id: int) -> bool:
        return self.session.query(
            exists().where(entities.Cart.user_id == user_id)).scalar()

    def cart_exists(self, cart_id: int) -> bool:
        return self.session.query(
            exists().where(entities.Cart.id == cart_id)).scalar()

    def get_article(self, cart_id: int, article_id: int) -> entities.Item:
        return self.session.query(entities.Item) \
            .filter(entities.Item.cart_id == cart_id) \
            .filter(entities.Item.article_id == article_id) \
            .one_or_none()
