#!/usr/bin/env python3
"""Integrate polynomials represented by coefficient lists."""


def poly_integral(poly, C=0):
    """Return the coefficient list for the integral of poly plus C."""
    if (not isinstance(poly, list) or not poly or
            any(not isinstance(coefficient, (int, float)) or
                isinstance(coefficient, bool) for coefficient in poly) or
            not isinstance(C, int) or isinstance(C, bool)):
        return None
    integral = [C]
    integral.extend(coefficient / (power + 1)
                    for power, coefficient in enumerate(poly))
    integral = [int(coefficient) if coefficient.is_integer() else coefficient
                if isinstance(coefficient, float) else coefficient
                for coefficient in integral]
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
