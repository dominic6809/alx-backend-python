#!/usr/bin/env python3
"""
This module contains a function to measure the execution time
of an async coroutine.
"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time.

    Arguments:
        n (int): The number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        float: The average time per execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
