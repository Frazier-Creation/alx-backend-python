#!/usr/bin/env python3
# 9-element_length.py
"Contains a function with annotated parameters and
return values with appropriate types."
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]