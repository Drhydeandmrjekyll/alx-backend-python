#!/usr/bin/env python3
"""
Module with measure_time function.
"""

import time
from typing import List
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay).

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Total elapsed time.
    """
    start_time = time.time()

    async def run_wait_n():
        return await wait_n(n, max_delay)

    # Run async function using run
    run(run_wait_n())

    end_time = time.time()
    total_time = end_time - start_time

    # Return total elapsed time
    return total_time


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
