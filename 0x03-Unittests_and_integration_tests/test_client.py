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

    @patch('client.get_json')
    @patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test public_repos method of GithubOrgClient class
        """
        # Define chosen payload
        payload = [{"name": "repo1"}, {"name": "repo2"}]

        # Mock return value of _public_repos_url
        mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/testorg/repos"
        )

        # Mock return value of get_json
        mock_get_json.return_value = payload

        # Create instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Call public_repos method
        result = client.public_repos()

        # Extract names of repositories from payload
        expected_repos = [repo['name'] for repo in payload]

        # Assert that result is expected list of repository names
        self.assertEqual(result, expected_repos)

        # Assert that _public_repos_url was called once
        mock_public_repos_url.assert_called_once()

        # Assert that get_json was called once with correct URL
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos")
