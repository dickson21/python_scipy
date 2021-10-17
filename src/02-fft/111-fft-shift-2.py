
"""
Subject : fft complex value signal
Created : 2020-08-24
Status : OK
Detail:
plots the FFT of two complex exponentials
note the asymmetric spectrum

Ref:
https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/fftpack.html
"""

import numpy as np 
from scipy.fftpack import fft, fftfreq, fftshift

# number of signal points
N = 400
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.exp(50.0 * 1.j * 2.0*np.pi*x) + 0.5*np.exp(-80.0 * 1.j * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)

import matplotlib.pyplot as plt
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()