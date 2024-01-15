#!/usr/bin/env python3
"""
Module with asynchronous coroutine wait_random.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
    asyncio.run(wait_random(5))
    asyncio.run(wait_random(15))
