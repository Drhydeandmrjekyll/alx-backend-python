#!/usr/bin/env python3
"""
Module containing unit tests for utils.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test get_json function with mocked requests.get
        """
        # Set up mock behavior
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # Call function
        result = get_json(test_url)

        # Assertions
        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
