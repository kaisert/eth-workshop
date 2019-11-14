import json
import requests
from swagger_server.exceptions.exceptions import UnexpectedStatusCode


def make_post_request(url, data=None):
    response = requests.post(f'http://{url}', json=data)
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return 200
    else:
        raise UnexpectedStatusCode(response.status_code)


def make_put_request(url, data=None):
    response = requests.put(f'http://{url}', json=data)
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return 200
    else:
        raise UnexpectedStatusCode(response.status_code)


def make_get_request(url):
    response = requests.get(f'http://{url}')
    if response.status_code == 200:
        return response.json()
    else:
        raise UnexpectedStatusCode(response.status_code)


def make_delete_request(url):
    response = requests.delete(f'http://{url}')
    if response.status_code == 200:
        return 200
    else:
        raise UnexpectedStatusCode(response.status_code)
