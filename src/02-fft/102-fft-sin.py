
"""
informal introduction to python
https://docs.python.org/2/tutorial/introduction.html

numpy linspace
https://numpy.org/devdocs/reference/generated/numpy.linspace.html



"""

import numpy as np 
#from numpy.fft import *
from numpy.dual import fft #OK
# Number of sample points #OK-warning
import matplotlib.pyplot as plt

N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2) 
#N//2 - explicit floor division discards the fractional part

plt.subplot(2,1,1)
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()


"""
from scipy.fft import fft
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()

"""