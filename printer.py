import numpy as np
import matplotlib.pyplot as plt


def printer():
   x = np.arange(0, 3, 0.1)
   y = x**3 - 3.9*x**2 + 4.4*x - 1.4
   plt.plot(x, y)
   plt.grid(True)
   plt.show()


if __name__ == '__main__':
    printer()