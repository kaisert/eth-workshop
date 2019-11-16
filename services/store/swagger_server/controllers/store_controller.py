import connexion
import six

from swagger_server.models.article import Article  # noqa: E501
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

def get_article(articleId):  # noqa: E501
    """get_articles_by_ids

     # noqa: E501

    :param articleIds: IDs of articles that need to be fetched
    :type articleIds: List[int]

    :rtype: Article
    """
    try:
        return repository.get_article(articleId)
    except ArticleNotFoundException:
        return 'article not found', 404
    return

def create_article(body):
    """Create article

    This can only be done by the logged in user. # noqa: E501

    :param body: Created article object
    :type body: dict | bytes

    :rtype: Article
    """
    if connexion.request.is_json:
        body = Article.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            return repository.create_article(body)
        except ArticleAlreadyExistsException:
            return 'article already exists', 409
    return

def get_inventory():  # noqa: E501
    """get_inventory

     # noqa: E501


    :rtype: List[Article]
    """
    return repository.get_inventory()


def buy_article(articleId, quantity):
    try:
        repository.buy_article(articleId, quantity)
    except ArticleNotFoundException:
        return 'article not found', 404
    except ArticleOutOfStockException:
        return 'article out of stock', 409

