#!/usr/bin/env python3
"""
Module containing unit tests for client.py
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test has_license method of GithubOrgClient class
        """
        # Create instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Call has_license method with provided input
        result = client.has_license(repo, license_key)

        # Assert that result matches expected value
        self.assertEqual(result, expected_result)
