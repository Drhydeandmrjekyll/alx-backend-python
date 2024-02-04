#!/usr/bin/env python3
"""
Module containing unit tests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", org_payload, repos_payload, expected_repos)
    ])
    @patch('client.get_json')
    def test_public_repos(self, org, org_payload, repos_payload, expected_repos, mock_get_json):
        mock_get_json.side_effect = [org_payload, repos_payload]
        client = GithubOrgClient(org)
        self.assertEqual(client.org, org)
        self.assertEqual(client.public_repos(), expected_repos)

    @parameterized.expand([
        ("google", org_payload, repos_payload, apache2_repos)
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self, org, org_payload, repos_payload, apache2_repos, mock_get_json):
        mock_get_json.side_effect = [org_payload, repos_payload]
        client = GithubOrgClient(org)
        self.assertEqual(client.org, org)
        self.assertEqual(client.public_repos("apache-2.0"), apache2_repos)
