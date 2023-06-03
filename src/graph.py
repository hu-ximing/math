import matplotlib.pyplot as plt
import numpy as np
from math import *

x_min = -10
x_max = 10
x_step = 0.001


def f(x):
    return x**2*sin(x)


x_values = np.linspace(x_min, x_max, int((x_max - x_min) / x_step))
y_values = list(map(f, x_values))

plt.plot(x_values, y_values, label='f1')
plt.legend()
plt.show()
