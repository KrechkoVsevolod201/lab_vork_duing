import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

a = 0.0;
b = 3.0;
e = 0.0001
x = symbols('x')

def f(x):
   return x**3 - 3.9*x**2 + 4.4*x - 1.4


def bisection_method(function, a, b, eps, dlt):
   root = 0
   count = 0
   while True:
      count += 1
      fa = function.subs(x, a)
      c = 0.5 * (a + b)
      if (b - a) < 2 * eps:
         root = c
         break
      fc = function.subs(x, c)
      if fc == 0:
         root = c
         break
      if fa * fc < dlt:
         b = c
      else:
         a = c
      fa = fc
   print("Метод половинного деления")
   print("Найденный корень x* = " + str(root))
   print("Невязка f(x*) = " + str(function.subs(x, root)))
   print("Кол-во итераций = " + str(count))


if __name__ == '__main__':
    bisection_method(x**3 - 3.9*x**2 + 4.4*x - 1.4, a, b, e, 10**(-3))
