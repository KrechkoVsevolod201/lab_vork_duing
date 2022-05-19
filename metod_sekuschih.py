import matplotlib.pyplot as plt
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
   n=0
   while abs(f(x_prev)) > eps:
      x1 = x - f(x) / (f(x_prev) - f(x)) * (x_prev - x)
      x_prev = x1
      i += 1
      n += 1
   print("Найденный корень x =" + str(x1))
   print("Невязка f(x) = " + str(f(x1)))
   print("Кол-во итераций = " + str(n))
   return (" ")
# --------------------------------


a = int(input("Левая граница a="))
#print('\n')
b = int(input("Правая граница b="))
#print('\n')
x0 = int(input("Начальное приближение x="))
#print('\n')
x1 = secant(f, x0)

