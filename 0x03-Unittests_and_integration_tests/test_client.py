#!/usr/bin/env python3
"""
Module for testing the client module.
This module contains test cases for GithubOrgClient class,
including integration tests.
"""

import unittest
from typing import Dict
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
import requests


@parameterized_class([
    {
        'org_payload': org_payload,
        'repos_payload': repos_payload,
        'expected_repos': expected_repos,
        'apache2_repos': apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class fixtures before running tests.
        Mock requests.get to return example payloads from fixtures.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mocked get request"""
            # Mock response object
            mock_response = type('MockResponse', (), {'json': lambda: {}})()

            # Return org payload for org URL
            if url.endswith('/orgs/test-org'):
                mock_response.json = lambda: cls.org_payload
            # Return repos payload for repos URL
            elif url.endswith('/orgs/test-org/repos'):
                mock_response.json = lambda: cls.repos_payload

            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Remove class fixtures after running tests.
        Stop the patcher.
        """
        cls.get_patcher.stop()
