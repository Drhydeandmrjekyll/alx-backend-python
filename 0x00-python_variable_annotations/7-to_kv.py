#!/usr/bin/env python3
"""
Module with a type-annotated function to_kv that returns a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square
        of v as a float.
    """
    return k, float(v ** 2)
