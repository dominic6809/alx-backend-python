#!/usr/bin/env python3
"""
Module for creating a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Parameters:
    multiplier (float): The multiplier to apply.

    Returns:
    Callable[[float], float]: A function to multiply a float by the multiplier
    """
    def multiply(n: float) -> float:
        return multiplier * n

    return multiply
