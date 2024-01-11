#!/usr/bin/env python3
"""
Module with duck-typed annotations for the function
safe_first_element.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns first element of sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of sequence or None if
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
