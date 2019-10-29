# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Article(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, quantity: int=None, article_id: int=None):  # noqa: E501
        """Article - a model defined in Swagger

        :param quantity: The quantity of this Article.  # noqa: E501
        :type quantity: int
        :param article_id: The article_id of this Article.  # noqa: E501
        :type article_id: int
        """
        self.swagger_types = {
            'quantity': int,
            'article_id': int
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'article_id': 'articleId'
        }

        self._quantity = quantity
        self._article_id = article_id

    @classmethod
    def from_dict(cls, dikt) -> 'Article':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Article of this Article.  # noqa: E501
        :rtype: Article
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Article.


        :return: The quantity of this Article.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Article.


        :param quantity: The quantity of this Article.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def article_id(self) -> int:
        """Gets the article_id of this Article.


        :return: The article_id of this Article.
        :rtype: int
        """
        return self._article_id

    @article_id.setter
    def article_id(self, article_id: int):
        """Sets the article_id of this Article.


        :param article_id: The article_id of this Article.
        :type article_id: int
        """

        self._article_id = article_id
