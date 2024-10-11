#!/usr/bin/env python3
"""
Module for zooming an array.
"""


from typing import List, Tuple, Iterable


def zoom_array(lst: Iterable[int], factor: int = 2) -> List[int]:
    """
    Zooms into an array by repeating each element by a given factor.

    Params:
    lst (Iterable[int]): The list or tuple of integers to zoom.
    factor (int): The factor by which to zoom the array. Defaults to 2.

    Returns:
    List[int]: A new list with elements from lst repeated by the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
