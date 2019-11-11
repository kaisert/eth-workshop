import os
import contextlib

import sqlalchemy
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from swagger_server.models import user as domain
from swagger_server.repository import entities
from swagger_server.exceptions.exceptions import *

db_username = 'postgres'
db_password = 'NotMyBestIdea'
if 'DB' in os.environ:
    db_host = os.environ['DB']
else:
    db_host = 'localhost'
db_port = 5432
db_db = 'user'


db_string = f"postgres+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_db}"
print(db_string)

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

    def create_user(self, domain_user: domain.User):
        with get_session() as session:
            if self.user_exists(session, domain_user.username):
                raise UserAlreadyExistsException()
            user = entities.User.from_domain(domain_user)
            session.add(user)
            session.commit()

    def delete_user(self, username: str):
        with get_session() as session:
            if not self.user_exists(session, username):
                raise UserNotFoundException()
            session.query(entities.User) \
                .filter(entities.User.username == username) \
                .delete()
            session.commit()

    def get_user(self, username: str) -> domain.User:
        with get_session() as session:
            user = session.query(entities.User) \
                .filter(entities.User.username == username) \
                .one_or_none()
            if user is None:
                raise UserNotFoundException()
            return user.to_domain()

    def update_user(self, username: str, user: domain.User):
        user.id = None
        with get_session() as session:
            if not self.user_exists(session, username):
                raise UserNotFoundException

            session.query(entities.User) \
                .filter(entities.User.username == username) \
                .update(user.to_dict())
            session.commit()

    def user_exists(self, session: Session, username: str) -> bool:
        return session.query(
            exists().where(entities.User.username == username)).scalar()
