#!/usr/bin/python3
"""
    Program:        evalPolyTwo.py
    Author:         Peter Southwick
    Date:           07/06/16
    Description:    A Short program that evaluates the polynomial:
                    y = 3x^3 + 4x^2 + 8
"""

import matplotlib.pyplot as plot
import numpy as np
from numpy.polynomial.polynomial import polyval


xi = -10    # Initial x value
xf = 10     # Final x value
nx = 100    # Number of x values we want
coeff = np.array([8, 0, 4, 3])

x = np.linspace(xi, xf, nx)
y = polyval(x, coeff)

line, = plot.plot(x, y)

plot.show()

for i in range(nx):
    print("{} {}".format(x[i], y[i]))