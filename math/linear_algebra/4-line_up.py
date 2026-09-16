#!/usr/bin/env python3
"""Add arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return the element-wise sum, or None for different shapes."""
    if len(arr1) != len(arr2):
        return None
    return [value1 + value2 for value1, value2 in zip(arr1, arr2)]
