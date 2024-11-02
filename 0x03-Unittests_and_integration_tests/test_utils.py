#!/usr/bin/env python3
"""
Module for testing the utils module.
This module contains test cases for utility functions,
specifically the access_nested_map function.
"""

import unittest
from typing import Dict, Tuple, Any
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                             path: Tuple[str, ...],
                             expected: Any) -> None:
        """Test access_nested_map returns correct values for different inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
