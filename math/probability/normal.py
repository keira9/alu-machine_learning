#!/usr/bin/env python3
"""Normal distribution functions."""

PI = 3.1415926536
E = 2.7182818285


def erf_approx(value):
    """Approximate the error function without external modules."""
    sign = 1
    if value < 0:
        sign = -1
    value = abs(value)
    t_value = 1 / (1 + 0.3275911 * value)
    polynomial = (((((1.061405429 * t_value - 1.453152027) * t_value +
                     1.421413741) * t_value - 0.284496736) * t_value +
                   0.254829592) * t_value)
    return sign * (1 - polynomial * E ** (-value ** 2))


class Normal:
    """Represent a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the distribution from data or parameters."""
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
            variance = sum((value - self.mean) ** 2 for value in data)
            variance /= len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score for x."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value for z."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the probability density at x."""
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        return E ** exponent / (self.stddev * (2 * PI) ** 0.5)

    def cdf(self, x):
        """Calculate the cumulative probability through x."""
        z = (x - self.mean) / (self.stddev * 2 ** 0.5)
        return (1 + erf_approx(z)) / 2
