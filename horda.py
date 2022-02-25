import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

a = 0.0;
b = 3.0;
e = 0.0001


def f(x:float) -> float:
    return x**3 - 3.9*x**2 + 4.4*x - 1.4
# --------------------------------


def secant(f, x0: float, eps: float=1e-7 ) -> float:
   """
   solves f(x) = 0 by secant method with precision eps
   :param f: f
   :param x0: starting point
   :param eps: precision wanted
   :return: root of f(x) = 0
   """
   x = x0
   x_prev = x0 + 2 * eps
   i = 0
   while abs(x - x_prev) >= eps and i < 1e3:
      x1 = x - f(x) / (f(x_prev) - f(x)) * (x_prev - x)
      x_prev = x1
      i += 1
   return x1
# --------------------------------


x0 = int(input("x="))
x1 = secant(f, x0)
print(x1)
