import connexion
import six

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.models.cart import Cart  # noqa: E501
from swagger_server import util


def add_article_to_cart(userId, article):  # noqa: E501
    """add_article_to_cart

     # noqa: E501

    :param userId: 
    :type userId: int
    :param article: 
    :type article: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        article = Article.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def checkout_cart(userId):  # noqa: E501
    """checkout_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    return 'do some magic!'


def create_cart_for_user(userId):  # noqa: E501
    """create_cart_for_user

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    return 'do some magic!'


def empty_cart(userId):  # noqa: E501
    """empty_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    return 'do some magic!'


def get_cart_by_user_id(userId):  # noqa: E501
    """get_cart_by_user_id

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: Cart
    """
    return 'do some magic!'


def remove_article_from_cart(userId, articleId, quantity=None):  # noqa: E501
    """remove_article_from_cart

     # noqa: E501

    :param userId: 
    :type userId: int
    :param articleId: 
    :type articleId: int
    :param quantity: 
    :type quantity: int

    :rtype: None
    """
    return 'do some magic!'
