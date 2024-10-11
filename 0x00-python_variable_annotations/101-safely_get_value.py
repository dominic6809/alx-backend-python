#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary.
"""


from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely get a value from a dictionary.

    Parameters:
    dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None]): The value to return if the key is not found

    Returns:
    Union[T, None]: The value associated with the key, or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
