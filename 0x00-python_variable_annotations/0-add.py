#!/usr/bin/env python3
"""
Module with a type-annotated function add that takes two float arguments
and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    Adds two float numbers.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of a and b.
    """
    return a + b
