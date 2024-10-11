#!/usr/bin/env python3
"""
Module for safely getting the first element of a sequence.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of a sequence.

    Params:
    lst (Sequence[Any]): A sequence from which to retrieve the first element.

    Returns:
    Union[Any, None]: The first element of the sequence, or None
    """
    if lst:
        return lst[0]
    else:
        return None
