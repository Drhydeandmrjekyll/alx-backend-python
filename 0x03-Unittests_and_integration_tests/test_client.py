#!/usr/bin/env python3
"""
Module containing unit tests for client.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method of GithubOrgClient class
        """
        # Create instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call org method
        client.org()

        # Assert that get_json is called once with expected argument
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
