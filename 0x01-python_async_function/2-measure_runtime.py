#!/usr/bin/env python3
"""
Module with measure_time function.
"""

import time
import asyncio

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
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
