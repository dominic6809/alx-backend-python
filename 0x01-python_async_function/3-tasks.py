#!/usr/bin/env python3
"""
module that contains a function that creates an asyncio.Task for wait_random.
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Arguments:
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        asyncio.Task: A task that will execute the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
