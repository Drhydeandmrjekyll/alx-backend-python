#!/usr/bin/env python3
"""
Module with measure_runtime coroutine.
"""

from asyncio import gather, run
from time import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in paralle
    and measures the total runtime.
    """
    start_time = time()
    await gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
