#!/usr/bin/env python3
"""
The module contains an asynchronous coroutine
that spawns multiple task_wait_random coroutines
and returns the list of delays in ascending order.
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay to pass to task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
