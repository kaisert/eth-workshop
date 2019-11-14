import connexion
import six

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.cart import Cart  # noqa: E501
from swagger_server import util

from swagger_server.repository.repository import Repository
from swagger_server.exceptions.exceptions import NotFoundException


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
        article = Item.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            with Repository() as repository:
                cart = repository.get_cart(userId)
                repository.add_item(cart.id, article)
        except NotFoundException:
            return 404
        return


def checkout_cart(userId):  # noqa: E501
    """checkout_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    try:
        with Repository() as repository:
            return repository.checkout_cart(userId)
    except NotFoundException:
        return 404


def create_cart_for_user(userId):  # noqa: E501
    """create_cart_for_user

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    with Repository() as repository:
        repository.create_cart(userId)
    return


def empty_cart(userId):  # noqa: E501
    """empty_cart

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: None
    """
    try:
        with Repository() as repository:
            repository.delete_cart(userId)
        return
    except NotFoundException:
        return 404


def get_cart_by_user_id(userId):  # noqa: E501
    """get_cart_by_user_id

     # noqa: E501

    :param userId: 
    :type userId: int

    :rtype: Cart
    """
    try:
        with Repository() as repository:
            return repository.get_items(userId)
    except NotFoundException:
        return 404


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
        with Repository() as repository:
            return repository.remove_item(userId, articleId)
    except NotFoundException:
        return 404
