import os
import contextlib
from typing import List

import sqlalchemy
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
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

entities.Base.metadata.drop_all(engine)
entities.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


@contextlib.contextmanager
def get_session():
    with contextlib.closing(Session()) as session:
        yield session


class Repository:
    def __init__(self):
        pass

    def create_cart(self, user_id: int) -> int:
        with get_session() as session:
            if not self.user_exists(session, user_id):
                cart = entities.Cart()
                session.add(cart)
                session.commit()
                return cart.id
            else:
                session.query(entities.Cart) \
                    .filter(entities.Cart.user_id == user_id) \
                    .one_or_none()

    def delete_cart(self, user_id: int):
        with get_session() as session:
            if not self.user_exists(session, user_id):
                raise NotFoundException()
            session.query(entities.Cart) \
                .filter(entities.Cart.user_id == user_id) \
                .delete()
            session.commit()

    def get_items(self, user_id: int) -> List[domain.Article]:
        with get_session() as session:
            articles = session.query(entities.Item) \
                .filter(entities.Item.cart.user_id == user_id)
            if articles is None or len(articles) == 0:
                raise NotFoundException()
            return [a.to_domain() for a in articles]

    def add_item(self, cart_id: int, article: domain.Article):
        with get_session() as session:
            if not self.article_exists(session, cart_id, article.article_id):
                article = entities.Item()
                article.article_id = article.article_id
                article.quantity = article.quantity
                session.add(article)
            else:
                article = session.query(entities.Item) \
                    .filter(entities.Item.article_id == article.article_id)
                article.quantity += article.quantity

            session.commit()

    def remove_item(self, user_id: int, article_id: int):
        with get_session() as session:
            if not self.user_exists(session, user_id):
                raise NotFoundException()

            session.query(entities.Cart) \
                .filter(entities.Item.cart.user_id == user_id and
                        entities.Item.article_id == article_id) \
                .delete()
            session.commit()

    def checkout_cart(self, cart_id: int) -> List[domain.Article]:
        articles = self.get_items(cart_id)
        self.delete_cart(cart_id)
        return articles

    def user_exists(self, session: Session, user_id: int) -> bool:
        return session.query(
            exists().where(entities.Cart.user_id == user_id)).scalar()

    def cart_exists(self, session: Session, cart_id: int) -> bool:
        return session.query(
            exists().where(entities.Cart.id == cart_id)).scalar()

    def article_exists(self, session: Session, cart_id: int, article_id: int) \
            -> bool:
        return session.query(
            exists().where(entities.Item.cart_id == cart_id and
                           entities.Item.article_id == article_id)).scalar()
