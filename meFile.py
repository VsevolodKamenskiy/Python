import numpy as np
from matplotlib import pyplot as plt
import math

print('Введите m:')
m = int(input())

dx = math.pi / 2880
x = math.pi / 6

x_data = []
y_data = []


def func(x):
    sum = 0.5
    i = 1
    while i <= m:
        b = (math.pow(-1, (i + 1)) + 1) / (math.pi * i)
        sum += b * math.sin(x * i)
        i += 1

    return sum

xmin = 0
xmax = 7

x_data = np.arange(xmin, xmax, dx)
y_data = [func(x) for x in x_data]


plt.plot(x_data, y_data)
plt.grid(True)
plt.axis('equal')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('M = ' + str(m))
plt.show()