#!/usr/bin/env python3
"""Exponential distribution."""

from math import exp


class Exponential:
    """Represent an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            self.lambtha = float(lambtha)
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """Calculate the probability density at x."""
        if x < 0:
            return 0
        return self.lambtha * exp(-self.lambtha * x)

    def cdf(self, x):
        """Calculate the cumulative probability through x."""
        if x < 0:
            return 0
        return 1 - exp(-self.lambtha * x)
