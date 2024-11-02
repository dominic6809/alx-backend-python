#!/usr/bin/env python3
"""
Module for testing the utils module.
This module contains test cases for utility functions,
including access_nested_map, get_json functions,
and memoize decorator.
"""

import unittest
from typing import Dict, Tuple, Any, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        """
        Test access_nested_map returns correct values for different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str, ...],
            expected: str) -> None:
        """Test access_nested_map raises KeyError for invalid inputs."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected}'")


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test get_json returns correct output and makes correct HTTP calls.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator"""

    def test_memoize(self) -> None:
        """
        Test that when calling a_property twice, a_method is only called once.
        """
        class TestClass:
            """Test class for memoization"""

            def a_method(self) -> int:
                """Method to be memoized"""
                return 42

            @memoize
            def a_property(self) -> int:
                """Property that uses memoization"""
                return self.a_method()

        test_obj = TestClass()

        # Mock a_method
        with patch.object(TestClass, 'a_method', 
                  return_value=42) as mock_method:
            # Call a_property twice
            first_call = test_obj.a_property
            second_call = test_obj.a_property

            # Assert method returns correct value
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)

            # Assert a_method was only called once
            mock_method.assert_called_once()
