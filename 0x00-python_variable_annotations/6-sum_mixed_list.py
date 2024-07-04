#!/usr/bin/env python3
"""Complex typpe - mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list"""
    return sum(mxd_lst)