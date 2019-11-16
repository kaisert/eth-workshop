import os
import contextlib
from typing import List

import sqlalchemy
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from swagger_server.models import article as domain
from swagger_server.models.articles import Articles
from swagger_server.repository import entities
from swagger_server.exceptions.exceptions import *

db_username = 'postgres'
db_password = 'NotMyBestIdea'
if 'DB' in os.environ:
    db_host = os.environ['DB']
else:
    db_host = 'localhost'
db_port = 5432
db_db = 'store'

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

    def create_article(self, domain_article: domain.Article) -> domain.Article:
        with get_session() as session:
            if self.article_exists(session, domain_article.id):
                raise ArticleAlreadyExistsException()
            article = entities.Article.from_domain(domain_article)
            session.add(article)
            session.commit()
            return article.to_domain()

    def get_article(self, id: str):
        with get_session() as session:
            article = session.query(entities.Article) \
                .filter(entities.Article.id == id) \
                .one_or_none()
            if article is None:
                raise ArticleNotFoundException()
            return article.to_domain()

    def get_articles(self, ids: List[int]) -> List[domain.Article]:
        with get_session() as session:
            articles = session.query(entities.Article) \
                .filter(entities.Article.id in ids) \
                .all()
            if len(articles) != len(ids):
                raise ArticleNotFoundException()
            return list(map(lambda a: a.to_domain(), articles))

    def get_inventory(self) -> List[domain.Article]:
        with get_session() as session:
            articles = session.query(entities.Article) \
                .filter(entities.Article.storage_quantity > 0) \
                .all()
            return list(map(lambda a: a.to_domain(), articles))

    def buy_article(self, article_id: int, quantity: int):
        with get_session() as session:
            article = session.query(entities.Article) \
                .filter(entities.Article.id == article_id) \
                .one_or_none()
            if article is None:
                raise ArticleNotFoundException

            if article.quantity < quantity:
                raise ArticleOutOfStockException
            else:
                article.quantity -= quantity
                session.commit()

    def article_exists(self, session: Session, id: str) -> bool:
        return session.query(
            exists().where(entities.Article.id == id)).scalar()