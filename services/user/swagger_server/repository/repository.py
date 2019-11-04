import contextlib

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from swagger_server.models import user as domain
from swagger_server.repository import entities

db_username = 'postgres'
db_password = 'NotMyBestIdea'
db_host = 'localhost'
db_port = 5432
db_db = 'user'

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

    def CreateUser(self, domain_user: domain.User):
        with get_session() as session:
            user = entities.User()
            user.first_name = domain_user.first_name
            user.last_name = domain_user.last_name
            user.email = domain_user.email
            user.password = domain_user.password
            user.username = domain_user.username
            session.add(user)
            session.commit()
