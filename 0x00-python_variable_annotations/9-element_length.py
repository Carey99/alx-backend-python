#!/usr/bin/env python3
"""Let's duck type an iterable object"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function element_length that takes an iterable lst as
    argument and returns a list of tuples, each tuple containing an element
    of the input iterable along with the length of the element.
    """
    return [(i, len(i)) for i in lst]
