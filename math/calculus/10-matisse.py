#!/usr/bin/env python3
"""Differentiate polynomials represented by coefficient lists."""


def poly_derivative(poly):
    """Return the coefficient list for the derivative of poly."""
    if (not isinstance(poly, list) or not poly or
            any(not isinstance(coefficient, (int, float)) or
                isinstance(coefficient, bool) for coefficient in poly)):
        return None
    if len(poly) == 1:
        return [0]
    derivative = [power * poly[power] for power in range(1, len(poly))]
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()
    return derivative
