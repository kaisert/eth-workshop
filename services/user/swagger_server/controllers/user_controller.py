import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

from swagger_server.repository.repository import Repository
from swagger_server.exceptions.exceptions import *

repository = Repository()


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            repository.create_user(body)
            return body
        except UserAlreadyExistsException:
            return 'user already exists', 409

    return 'Bad Request', 400


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    try:
        repository.delete_user(username)
    except UserNotFoundException:
        return 'user not found', 404
    return {}


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    try:
        return repository.get_user(username)
    except UserNotFoundException:
        return 'user not found', 404
