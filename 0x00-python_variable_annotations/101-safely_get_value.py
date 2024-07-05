#!/usr/bin/env python3
"""More involved type annotations"""


from typing import Tuple, List


def safely_get_value(dct: dict, key: str, default: int = 0) -> Tuple:
    """Return a tuple containing the value and the key"""
    if key in dct:
        return (dct[key], key)
    else:
        return (default, key)
