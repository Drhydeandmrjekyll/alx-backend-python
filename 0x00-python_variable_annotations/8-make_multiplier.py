#!/usr/bin/env python3
"""
Module with a type-annotated function make_multiplier that returns function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns function that multiplies float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: Function that takes float and returns
        the product.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
