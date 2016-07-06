#!/usr/bin/python3
"""
    Program:        evalPolyOne.py
    Author:         Peter Southwick
    Date:           07/06/16
    Description:    A Short program that evaluates the polynomial:
                    y = x^4 + 4x^2 + 7
"""

import matplotlib.pyplot as plot
import numpy as np
from numpy.polynomial.polynomial import polyval


xi = -100    # Initial x value
xf = 100     # Final x value
nx = 100    # Number of x values we want
coeff = np.array([7, 0, 4, 0, 1])

x = np.linspace(xi, xf, nx)
y = polyval(x, coeff)

line, = plot.plot(x, y)

plot.show()

for i in range(nx):
    print("{} {}".format(x[i], y[i]))
