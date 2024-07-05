#!/usr/bin/env python3
"""More involved type annotations"""


from typing import Any, TypeVar, Union, Mapping, Tuple, Dict


T = TypeVar('T')
ResponseType = Union[T, None]
Def1 = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def1 = 0) -> ResponseType:
    """Return a tuple containing the value and the key"""
    if key in dct:
        return (dct[key])
    else:
        return (default)
