#!/usr/bin/env python3
"""
Module for summing a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum all elements in a list of floats.

    Params:
    input_list (List[float]): A list of floats to sum.

    Returns:
    float: The sum of the floats in the list.
    """
    return sum(input_list)
