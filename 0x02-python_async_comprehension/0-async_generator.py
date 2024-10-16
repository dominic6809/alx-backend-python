#!/usr/bin/env python3


import asyncio
import random
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
