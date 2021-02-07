import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20

def my_asin(x):
    
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, ITERATIONS):
        x_pow *= x**2
        multiplier *= 2*n*(2*n-1)**2 / 4 / n**2 / (2*n + 1)
        partial_sum += x_pow * multiplier
    return partial_sum

print(math.asin(0.4))
print(my_asin(0.4))

# %matplotlib inline
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')

vs = np.vectorize(my_asin)
print(my_asin, vs)

angles = np.r_[-1:1:0.001]
plt.plot(angles, np.arcsin(angles))
plt.plot(angles, vs(angles))

ax = plt.axes()
ax.set_xticks(np.arange(-1, 1 + 0.1, 1))
ax.set_yticks(np.arange(-1, 2, 1))
ax.set_xticks(np.arange(-1, 2, 0.5), minor=True)
ax.set_yticks(np.arange(-1, 2, 0.5), minor=True)
ax.grid(which='minor', alpha=0.5)
ax.grid(which='major', alpha=0.5, color='black')

plt.show()
