from pathlib import Path

from swagger_server.services.http import *

base_url = Path('shopping_cart:8080/cart')


def add_article(userId, item):
    url = Path(f'{userId}/article')
    make_post_request(base_url / url, item)


def checkout(userId):
    url = Path(f'{userId}/checkout')
    return make_post_request(base_url / url)


def create_for_user(userId):
    url = Path(f'{userId}')
    return make_post_request(base_url / url)


def empty(userId):
    url = Path(f'{userId}')
    make_delete_request(base_url / url)


def get_by_user_id(userId):
    url = Path(f'{userId}')
    return make_get_request(base_url / url)


def remove_article(userId, articleId):
    url = Path(f'{userId}/article/{articleId}')
    return make_delete_request(base_url / url)
