import connexion
import six

from swagger_server.models.articles import Articles  # noqa: E501
from swagger_server import util

from swagger_server.repository.repository import Repository
from swagger_server.exceptions.exceptions import *

repository = Repository()


def get_articles_by_ids(articleIds):  # noqa: E501
    """get_articles_by_ids

     # noqa: E501

    :param articleIds: IDs of articles that need to be fetched
    :type articleIds: List[int]

    :rtype: Articles
    """
    try:
        articles = repository.get_articles(articleIds)
    except ArticleNotFoundException:
        return 'article not found', 404
    return articles


def get_inventory():  # noqa: E501
    """get_inventory

     # noqa: E501


    :rtype: Articles
    """
    articles = repository.get_inventory()
    return articles


def buy_article(articleId, quantity):
    try:
        repository.buy_article(articleId, quantity)
    except ArticleNotFoundException:
        return 'article not found', 404
    except ArticleOutOfStockException:
        return 'article out of stock', 409

