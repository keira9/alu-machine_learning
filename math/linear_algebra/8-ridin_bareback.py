#!/usr/bin/env python3
"""Multiply two-dimensional matrices."""


def mat_mul(mat1, mat2):
    """Return the matrix product, or None for incompatible matrices."""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(left * right for left, right in zip(row, column))
             for column in zip(*mat2)] for row in mat1]
