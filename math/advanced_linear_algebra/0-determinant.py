#!/usr/bin/env python3
"""Calculate the determinant of a square matrix."""


def _validate_matrix(matrix):
    """Validate a matrix and return its size."""
    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 0
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a square matrix")
    return size


def determinant(matrix):
    """Return the determinant of matrix."""
    size = _validate_matrix(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    for column in range(size):
        submatrix = [row[:column] + row[column + 1:]
                     for row in matrix[1:]]
        sign = -1 if column % 2 else 1
        result += sign * matrix[0][column] * determinant(submatrix)
    return result
