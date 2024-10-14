#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay betn 0 and max_delay seconds and returns the delay

    Arguments:
        max_delay (int): Maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
