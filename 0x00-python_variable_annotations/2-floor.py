#!/usr/bin/env python3
"""
Module for calculating the floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Params:
    n (float): The float to find the floor of.

    Returns:
    int: The largest integer less than or equal to n.
    """
    return math.floor(n)
