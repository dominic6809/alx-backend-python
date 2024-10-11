#!/usr/bin/env python3
"""
Module for converting a key and value into a tuple with the key and the square
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key and value into a tuple.

    Params:
    k (str): A string key.
    v (Union[int, float]): An integer or float value.

    Returns:
    Tuple[str, float]: tuple(1st element=str key& the 2nd element is the square
    """
    return (k, float(v ** 2))
