#!/usr/bin/env python3
"""Duck typing - first element of a sequence
"""


from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type-annotated function safe_first_element that takes a lst of any
    type elements and returns the first element of the list if there is any,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
