#!/usr/bin/env python3
"""
Module with async coroutine wait_random.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay, with default value of 10)
    named wait_random that waits for random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Random delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
