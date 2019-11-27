import connexion
import six

from swagger_server.models.user import User  # noqa: E501

from swagger_server.exceptions.exceptions import *
from swagger_server.services.http import *

from pathlib import Path


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        try:
            create_user(body)
        except UnexpectedStatusCode as e:
            return e.code


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    try:
        delete_user(username)
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
    try:
        return get_user_by_name(username)
    except UnexpectedStatusCode as e:
        return e.code
