#!/usr/bin/env python3
"""
Module with asynchronous coroutine wait_n.
"""

import asyncio
from typing import List
import importlib

async_syntax_module = importlib.import_module("0-basic_async_syntax")
wait_random = async_syntax_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns wait_random n times
    with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
