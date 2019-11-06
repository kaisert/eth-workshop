import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

import swagger_server.models as domain

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    # user_status =

    def to_domain(self) -> domain.User:
        dictionary = vars(self)
        dictionary['firstName'] = self.first_name
        dictionary['lastName'] = self.last_name
        return domain.User.from_dict(vars(self))

    @classmethod
    def from_domain(cls, domain_user: domain.User):
        user = User()
        user.first_name = domain_user.first_name
        user.last_name = domain_user.last_name
        user.email = domain_user.email
        user.password = domain_user.password
        user.username = domain_user.username
        return user
