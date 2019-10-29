# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.models.cart import Cart  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_article_to_cart(self):
        """Test case for add_article_to_cart

        
        """
        article = Article()
        response = self.client.open(
            '/cart/{userId}/article'.format(userId=789),
            method='POST',
            data=json.dumps(article),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_checkout_cart(self):
        """Test case for checkout_cart

        
        """
        response = self.client.open(
            '/cart/{userId}/checkout'.format(userId=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_cart_for_user(self):
        """Test case for create_cart_for_user

        
        """
        response = self.client.open(
            '/cart/{userId}'.format(userId=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empty_cart(self):
        """Test case for empty_cart

        
        """
        response = self.client.open(
            '/cart/{userId}'.format(userId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cart_by_user_id(self):
        """Test case for get_cart_by_user_id

        
        """
        response = self.client.open(
            '/cart/{userId}'.format(userId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_article_from_cart(self):
        """Test case for remove_article_from_cart

        
        """
        query_string = [('quantity', 56)]
        response = self.client.open(
            '/cart/{userId}/article/{articleId}'.format(userId=789, articleId=56),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
