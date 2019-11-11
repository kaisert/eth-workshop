from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *

from swagger_server.models import article as domain

Base = declarative_base()


class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)
    items = relationship("items", back_populates="cart")


class Item(Base):
    __tablename__ = "items"
    article_id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), primary_key=True)
    quantity = Column(Integer)
    cart = relationship("carts", back_populates="items")

    def to_domain(self) -> domain.Article:
        article = domain.Article()
        article.quantity = self.quantity
        article.article_id = self.article_id
        return article
