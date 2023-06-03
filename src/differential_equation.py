import matplotlib.pyplot as plt
import numpy as np
from math import *

x_min = -10
x_max = 10
y_min = -10
y_max = 10
segment_len = 0.5
step = 1


def dydx(x, y):
    try:
        return x**2/y
    except ZeroDivisionError:
        return 1e10


fig = plt.figure()
# set grid
ax = fig.add_subplot(1, 1, 1)
x_grid_ticks = np.arange(x_min, x_max, 1)
y_grid_ticks = np.arange(y_min, y_max, 1)
ax.set_xticks(x_grid_ticks)
ax.set_yticks(y_grid_ticks)
plt.grid()
# make x=0 and y=0 lines visible
plt.axhline(y=0, color='k', alpha=0.5)
plt.axvline(x=0, color='k', alpha=0.5)

x = x_min
while x <= x_max:
    y = y_min
    while y <= y_max:
        slope = dydx(x, y)
        sub_domain = (segment_len / (slope**2 + 1))**0.5
        x1 = x - sub_domain / 2
        x2 = x + sub_domain / 2
        sub_range = slope * sub_domain
        y1 = y - sub_range / 2
        y2 = y + sub_range / 2
        plt.plot([x1, x2], [y1, y2], color='k')
        y += step
    x += step

plt.show()