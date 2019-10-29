import connexion
import six

from swagger_server.models.articles import Articles  # noqa: E501
from swagger_server import util


def get_articles_by_ids(articleIds):  # noqa: E501
    """get_articles_by_ids

     # noqa: E501

    :param articleIds: IDs of articles that need to be fetched
    :type articleIds: List[int]

    :rtype: Articles
    """
    return 'do some magic!'


def get_inventory():  # noqa: E501
    """get_inventory

     # noqa: E501


    :rtype: Articles
    """
    return 'do some magic!'
