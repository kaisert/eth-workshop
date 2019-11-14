import connexion
import six

from swagger_server.models.item import Item# noqa: E501
from swagger_server.models.cart import Cart  # noqa: E501
from swagger_server.services.http import *

from pathlib import Path

base_url = Path('shopping_cart:8080/cart')


def add_article_to_cart(userId, item):  # noqa: E501
    """add_article_to_cart

     # noqa: E501

    :param userId: 
    :type userId: int
    :param article: 
    :type article: dict | bytes

    :rtype: None
    """
    url = Path(f'{userId}/article')
    if connexion.request.is_json:
        try:
            make_post_request(base_url / url, item)
            return
        except UnexpectedStatusCode as e:
            return e.code


def checkout_cart(userId):  # noqa: E501
    """checkout_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    url = Path(f'{userId}/checkout')
    try:
        return make_post_request(base_url / url)
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
    url = Path(f'{userId}')
    try:
        make_post_request(base_url / url)
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
    url = Path(f'{userId}')
    try:
        make_delete_request(base_url / url)
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
    url = Path(f'{userId}')
    try:
        return make_get_request(base_url / url)
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
    url = Path(f'{userId}/article/{articleId}')
    try:
        return make_delete_request(base_url / url)
    except UnexpectedStatusCode as e:
        return e.code
