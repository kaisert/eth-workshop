import connexion
import six

from swagger_server.models.item import Item# noqa: E501
from swagger_server.models.cart import Cart  # noqa: E501
from swagger_server.services.cart_service import *


def add_article_to_cart(userId, item):  # noqa: E501
    """add_article_to_cart

     # noqa: E501

    :param userId: 
    :type userId: int
    :param article: 
    :type article: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            return add_article(userId, item)
        except UnexpectedStatusCode as e:
            return e.code


def checkout_cart(userId):  # noqa: E501
    """checkout_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    try:
        return checkout(userId)
    except UnexpectedStatusCode as e:
        return e.code
    pass


def create_cart_for_user(userId):  # noqa: E501
    """create_cart_for_user

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    try:
        create_for_user(userId)
        return
    except UnexpectedStatusCode as e:
        return e.code


def empty_cart(userId):  # noqa: E501
    """empty_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    try:
        empty(userId)
        return
    except UnexpectedStatusCode as e:
        return e.code


def get_cart_by_user_id(userId):  # noqa: E501
    """get_cart_by_user_id

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: Cart
    """
    try:
        return get_by_user_id(userId)
    except UnexpectedStatusCode as e:
        return e.code


def remove_article_from_cart(userId, articleId):  # noqa: E501
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
    try:
        return remove_article(userId, articleId)
    except UnexpectedStatusCode as e:
        return e.code
