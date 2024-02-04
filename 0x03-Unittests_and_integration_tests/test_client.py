#!/usr/bin/env python3
"""
Module containing unit tests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    def test_public_repos_url(self):
        """
        Test _public_repos_url property of GithubOrgClient class
        """
        # Define a known payload
        payload = {'repos_url': 'https://api.github.com/orgs/testorg/repos'}

        # Patch org property to return known payload
        with patch.object(
                GithubOrgClient,
                'org',
                PropertyMock(return_value=payload)):
            # Create instance of GithubOrgClient
            client = GithubOrgClient("testorg")

            # Get value of _public_repos_url
            result = client._public_repos_url

            # Assert that result is expected one based on mocked payload
            self.assertEqual(
                    result,
                    'https://api.github.com/orgs/testorg/repos')
