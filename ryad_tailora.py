{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "ITERATIONS = 20\n",
    "\n",
    "def my_asin(x):\n",
    "    x_pow = x\n",
    "    multiplier = 1\n",
    "    partial_sum = x\n",
    "    for n in range(1, ITERATIONS):\n",
    "        x_pow = x**2  \n",
    "        multiplier *= 2*n*(2*n-1)**2 / 4 / n**2 / (2*n + 1) \n",
    "        partial_sum += x_pow * multiplier\n",
    "        plt.plot (n, partial_sum)\n",
    "    return partial_sum\n",
    "\n",
    "print (math.asin(0.4))\n",
    "print (my_asin(0.4))\n",
    "\n",
    "import matplotlob.pyplot as plt\n",
    "import numpy as np\n",
    "fig = plt.figure\n",
    "ax = fig.add_subplot(1, 1, 1)\n",
    "\n",
    "major_ticks = np.arange(-5, 5, 1) \n",
    "minor_ticks = np.arange(-5.5, 5.5, 1) \n",
    "\n",
    "ax.set_xticks(major_ticks)\n",
    "ax.set_xticks(minor_ticks, minor=True)\n",
    "ax.set_yticks(major_ticks)\n",
    "ax.set_yticks(minor_ticks, minor=True)\n",
    "\n",
    "ax.grid(which='minor', alpha=0.2)\n",
    "ax.grid(which='major', alpha=0.5)\n",
    "\n",
    "from IPython.display import set_matplotlib_formats\n",
    "set_matplotlib_formats('pdf', 'svg')\n",
    "\n",
    "vs = np.vectorize(my_asin)\n",
    "print(my_asin, vs)\n",
    "\n",
    "angles = np.r_[-1:1:0.001]\n",
    "plt.plot(angles, vs(angles))\n",
    "\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
