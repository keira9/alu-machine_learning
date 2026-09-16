#!/usr/bin/env python3
"""Perform element-wise operations on NumPy arrays."""
import numpy as np


def np_elementwise(mat1, mat2):
    """Return the sum, difference, product, and quotient."""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
