#!/usr/bin/env python3
"""
Module with measure_time function.
"""

import time
from typing import List
from asyncio import run
from concurrent.futures import ProcessPoolExecutor

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average execution time per iteration.
    """
    start_time = time.time()

    async def run_wait_n():
        return await wait_n(n, max_delay)

    # Run async function in separate process to bypass Global Interpreter Lock
    with ProcessPoolExecutor() as executor:
        delays: List[float] = run(executor.submit(run_wait_n))

    end_time = time.time()
    total_time = end_time - start_time

    # Returns average execution time per iteration
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))