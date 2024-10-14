#!/usr/bin/env python3
"""
The module contains an asynchronous coroutine
that spawns multiple wait_random coroutines
and returns the list of delays in ascending order.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of delays
    in ascending order without using sort().

    Arguments:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
