#!/usr/bin/env python3

from typing import Tuple


def zoom_array(lst: Tuple[int], factor: float = 2) -> Tuple[int]:
    zoomed_in: Tuple[int] = tuple(
        item for item in lst
        for _ in range(int(factor))
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
