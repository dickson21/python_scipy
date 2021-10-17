
"""
Subject : blackman window signal
Create : 2020-08-24
Status : OK
ref:
fourier transform
https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/fftpack.html

"""

import numpy as np 
from numpy.fft import fft, fftshift
import matplotlib.pyplot as plt

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
#from scipy.signal import blackman
w = np.blackman(N)
ywf = fft(y*w)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#import matplotlib.pyplot as plt
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), '-r')
plt.legend(['FFT', 'FFT w. window'])
plt.grid()
plt.show()