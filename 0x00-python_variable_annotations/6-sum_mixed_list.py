#!/usr/bin/env python3
"""
Module with type-annotated function sum_mixed_list that returns sum of list
of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): Input list of integers and floats.

    Returns:
        float: Sum of input list.
    """
    return sum(mxd_lst)
