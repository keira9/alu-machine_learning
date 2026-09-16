#!/usr/bin/env python3
"""Calculate the inverse of a square matrix."""


def _validate_matrix(matrix):
    """Validate a non-empty square matrix."""
    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")


def _determinant(matrix):
    """Calculate a determinant for a validated matrix."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    for column in range(size):
        submatrix = [row[:column] + row[column + 1:] for row in matrix[1:]]
        sign = -1 if column % 2 else 1
        result += sign * matrix[0][column] * _determinant(submatrix)
    return result


def inverse(matrix):
    """Return the inverse of matrix, or None if it is singular."""
    _validate_matrix(matrix)
    size = len(matrix)
    determinant = _determinant(matrix)
    if determinant == 0:
        return None
    if size == 1:
        return [[1 / determinant]]
    cofactors = []
    for row_index in range(size):
        row = []
        for column_index in range(size):
            submatrix = [row_data[:column_index] + row_data[column_index + 1:]
                         for index, row_data in enumerate(matrix)
                         if index != row_index]
            value = _determinant(submatrix)
            if (row_index + column_index) % 2 == 0:
                row.append(value)
            else:
                row.append(-value)
        cofactors.append(row)
    adjugate = zip(*cofactors)
    return [[value / determinant for value in row] for row in adjugate]
