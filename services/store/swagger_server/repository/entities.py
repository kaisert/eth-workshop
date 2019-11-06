from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

import swagger_server.models as domain

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    description = Column(String, unique=True)
    storage_quantity = Column(Integer)
    next_ship_date = Column(String)

    def to_domain(self) -> domain.Article:
        dictionary = vars(self)
        dictionary['inStorage'] = self.storage_quantity > 0
        dictionary['nextShipDate'] = self.next_ship_date
        return domain.Article.from_dict(vars(self))

    @classmethod
    def from_domain(cls, domain_article: domain.Article):
        article = Article()
        article.description = domain_article.description

        return article
