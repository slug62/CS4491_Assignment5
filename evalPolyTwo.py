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


xi = -5    # Initial x value
xf = 5     # Final x value
nx = 50     # Number of x values we want
coeff = np.array([8, 0, 4, 3])

x = np.linspace(xi, xf, nx)     # Create a list of evenly spaced x values using numpy linspace function
y = polyval(x, coeff)           # Evaluate the polynomial

line, = plot.plot(x, y)         # Use MATPLOTLIB to plot the graph

plot.show()                     # Display the graph

print("Coeffcient list: ")
print(coeff)

print("X and Y Pairs")
for i in range(nx):             # Display the x and y values
    print("({}, {})".format(x[i], y[i]))

