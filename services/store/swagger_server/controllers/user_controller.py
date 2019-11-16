import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

from swagger_server.exceptions.exceptions import *
from swagger_server.services.http import *

from pathlib import Path

base_url = Path('user:8080/user')

def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        url = Path(f'')
        try:
            return make_post_request(base_url / url, body)
        except UnexpectedStatusCode as e:
            return e.code


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    url = Path(f'{username}')
    try:
        make_delete_request(base_url / url)
        return {}
    except UnexpectedStatusCode as e:
        return e.code


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    url = Path(f'{username}')
    try:
        return make_get_request(base_url / url)
    except UnexpectedStatusCode as e:
        return e.code
