#!/usr/bin/env python3
"""
Module with async comprehension.
"""

from typing import List
from random import uniform
from asyncio import gather


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that uses async comprehension to collect 10
    random numbers from async_generator.
    """
    return [i async for i in async_generator()]
