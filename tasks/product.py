from typing import Any
from itertools import product
__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
     return list(product(arr1, arr2))
