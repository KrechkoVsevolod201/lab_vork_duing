import matplotlib.pyplot as plt
import numpy as np
import sys
import math
from sympy import *

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
   print("----------------Метод половинного деления----------------")
   print("Найденный корень x* = " + str(root))
   print("Невязка f(x*) = " + str(function.subs(x, root)))
   print("Кол-во итераций = " + str(count))



def f(x:float) -> float:
    return x**3 - 3.9*x**2 + 4.4*x - 1.4
# --------------------------------


def secant(f, a, b, x0: float, eps: float=1e-7 ) -> float:
   """
   solves f(x) = 0 by secant method with precision eps
   :param f: f
   :param x0: starting point
   :param eps: precision wanted
   :return: root of f(x) = 0
   """
   x = x0
   x_prev = x0 - 2 * eps
   i = 0
   n=0
   while abs(f(x_prev)) > eps:
      x1 = x - f(x) / (f(x_prev) - f(x)) * (x_prev - x)
      x_prev = x1
      i += 1
      n += 1
      if x1 > b:
         print("----------------Метод секущих----------------")
         print("Введите новое начальное приближение")
         x = int(input("Начальное приближение x0="))

   print("----------------Метод секущих----------------")
   print("Найденный корень x =" + str(x1))
   print("Невязка f(x) = " + str(f(x1)))
   print("Кол-во итераций = " + str(n))
   return (" ")
# --------------------------------


def printer():
   x = np.arange(0, 3, 0.1)
   y = x**3 - 3.9*x**2 + 4.4*x - 1.4
   plt.plot(x, y)
   plt.grid(True)
   plt.show()


printer()
a = int(input("Левая граница a="))
b = int(input("Правая граница b="))
x0 = int(input("Начальное приближение x0="))
x2 = bisection_method(x**3 - 3.9*x**2 + 4.4*x - 1.4, a, b, e, 10**(-3))
x1 = secant(f, a, b, x0)

