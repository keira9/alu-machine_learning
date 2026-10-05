#!/usr/bin/env python3
"""Poisson distribution."""

from math import exp, factorial


class Poisson:
    """Represent a Poisson distribution."""

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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculate the probability of k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return (self.lambtha ** k * exp(-self.lambtha)) / factorial(k)

    def cdf(self, k):
        """Calculate the cumulative probability through k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(successes) for successes in range(k + 1))
