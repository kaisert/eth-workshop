from pathlib import Path

from swagger_server.services.http import *

base_url = Path('toxiproxy:8082/user')


def create_user(body):
    url = Path(f'')
    return make_post_request(base_url / url, body)


def delete_user(username):
    url = Path(f'{username}')
    make_delete_request(base_url / url)


def get_user_by_name(username):
    url = Path(f'{username}')
    return make_get_request(base_url / url)
