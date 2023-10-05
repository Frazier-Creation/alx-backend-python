#!/usr/bin/env python3
# 7-to_kv.py
"Contains a function that converts a Python variable to a KV pair."
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "Converts a Python variable to a KV pair."
    return k, v ** 2
