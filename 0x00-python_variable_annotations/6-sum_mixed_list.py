#!/usr/bin/env python3
"""
Module for summing a mixed list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all elements in a mixed list of integers and floats.

    Params:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
    float: The sum of the elements in the list as a float.
    """
    return float(sum(mxd_lst))
