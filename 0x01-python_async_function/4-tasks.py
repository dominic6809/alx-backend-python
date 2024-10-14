#!/usr/bin/env python3
"""
The module contains an asynchronous coroutine
that spawns multiple task_wait_random coroutines
and returns the list of delays in ascending order.
"""


import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of delays
    in ascending order without using sort().

    Arguments:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
