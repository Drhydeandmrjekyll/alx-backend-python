#!/usr/bin/env python3
"""
Module with async generator.
"""

import asyncio
import random
from typing import AsyncGenerator


async def numbers(limit: int) -> AsyncGenerator[float, None]:
    for _ in range(limit):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields random number between 0 and 10 after
    waiting 1 second, repeated 10 times.
    """
    async for num in numbers(10):
        yield num
