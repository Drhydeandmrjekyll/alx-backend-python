#!/usr/bin/env python3
"""
Module with task_wait_random function.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task for wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
