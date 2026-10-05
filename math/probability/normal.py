#!/usr/bin/env python3
"""Normal distribution."""

from math import erf, exp, pi, sqrt


class Normal:
    """Represent a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((value - self.mean) ** 2 for value in data) / len(data)
            self.stddev = float(sqrt(variance))

    def z_score(self, x):
        """Calculate the z-score for x."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value for z."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the probability density at x."""
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        return exp(exponent) / (self.stddev * sqrt(2 * pi))

    def cdf(self, x):
        """Calculate the cumulative probability through x."""
        z = (x - self.mean) / (self.stddev * sqrt(2))
        return (1 + erf(z)) / 2
