#!/usr/bin/env python3
""" 7-to_kv.py """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (str): STR
        v (Union[int, float]): Int OR float

    Returns:
        Tuple: _description_
    """
    n = v ** 2
    return (k, n)
