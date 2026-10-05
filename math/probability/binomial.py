#!/usr/bin/env python3
"""Binomial distribution functions."""


class Binomial:
    """Represent a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the distribution from data or parameters."""
        if data is None:
            self.n = int(n)
            self.p = float(p)
            if self.n <= 0:
                raise ValueError("n must be a positive value")
            if self.p <= 0 or self.p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((value - mean) ** 2 for value in data) / len(data)
            self.p = 1 - variance / mean
            self.n = round(mean / self.p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculate the probability of k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        combinations = 1
        for index in range(1, min(k, self.n - k) + 1):
            combinations = combinations * (self.n - index + 1) / index
        return combinations * self.p ** k * (1 - self.p) ** (self.n - k)

    def cdf(self, k):
        """Calculate the cumulative probability through k successes."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        return sum(self.pmf(successes) for successes in range(k + 1))
