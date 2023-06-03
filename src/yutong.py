import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1.044338,1.044338,10000)
y1=(x**2+np.sqrt(x**4-4*(x**6-1)))/2
y2=(x**2-np.sqrt(x**4-4*(x**6-1)))/2
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlim(-2,2)
plt.ylim(-2,2)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_visible(False)
ax.xaxis.set_visible(False)
plt.plot(x**3,y1,'red')
plt.plot(-x**3,y1,'red')
plt.plot(x**3,y2,'red')
plt.plot(-x**3,y2,'red')
plt.show()