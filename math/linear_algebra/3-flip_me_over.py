#!/usr/bin/env python3
"""Transpose a two-dimensional matrix."""


def matrix_transpose(matrix):
    """Return a new matrix containing the transpose of matrix."""
    return [list(column) for column in zip(*matrix)]
