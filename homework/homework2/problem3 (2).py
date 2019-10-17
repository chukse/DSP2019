from math import pi, exp, sqrt
import numpy as np

mu = 0.0
sigma = 2.0
x = 1.0


def Gaussian(mu, sigma, x):
    y = (1.0 / (sqrt(2.0 * pi) * sigma)) * exp(-(1.0 / 2.0) * ((x - mu) / sigma) ** 2.0)

    return y


answer = Gaussian(mu, sigma, x)
print(answer)