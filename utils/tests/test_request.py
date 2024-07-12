from importlib import import_module
import logging
import unittest
from unittest import TestCase

from utils.request import Response
from utils.request import request

import_module("utils.logger.init")

logger = logging.getLogger()


class TestRequest(TestCase):
    def test_request(self):
        """python -m unittest utils.tests.test_request.TestRequest.test_request"""

        URL = "https://httpbin.org/get"
        response: Response = request(URL, method="get")
        assert response.status == 200
        assert isinstance(response.body, str)
        logger.info(response.data)
        assert isinstance(response.data, dict)

        URL = "https://baidu.com"
        response: Response = request(URL, method="get")
        assert isinstance(response, Response)
        assert response.status == 200
        assert isinstance(response.body, str)
        logger.info(response.body[:100])
        logger.info(response.data)
        assert isinstance(response.data, dict)

    def test_response(self):
        """python -m unittest utils.tests.test_request.TestRequest.test_response"""
        from email.message import Message

        response = Response(body="{}", headers=Message(), status=200)
        logger.info(response)
        logger.info(response.status)
        logger.info(response.headers)
        logger.info(response.body)

        URL = "https://httpbin.org/get"
        response: Response = request(URL, method="get")
        assert isinstance(response, Response)
        assert response.status == 200
        logger.info(response.data)
        assert isinstance(response.data, dict)

    def test_multiple_request(self):
        """python -m unittest utils.tests.test_request.TestRequest.test_response_json"""

        request_tasks = {
            "get": "https://httpbin.org/get?foo=bar",
            "post": "https://httpbin.org/post",
            "patch": "https://httpbin.org/patch",
        }

        for method, url in request_tasks.items():
            response = request(url, method=method.upper(), data={"title": "foo", "body": method.upper()})
            logger.info(response.status)
            assert response.status == 200
            # logger.info(type(response.body))
            # logger.info(response.body)
            # logger.info(response.json())
            logger.info(response.data)
            assert isinstance(response.data, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
