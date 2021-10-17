"""
Subject : blackman window
Status : OK

ref:
blackman window
https://numpy.org/doc/stable/reference/generated/numpy.blackman.html

Ref:
https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/fftpack.html

"""


import numpy as np 
from numpy.fft import fft, fftshift
import matplotlib.pyplot as plt

window = np.blackman(51)
plt.figure()
A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
with np.errstate(divide='ignore', invalid='ignore'):
    response = 20 * np.log10(mag)

response = np.clip(response, -100, 100)
plt.plot(freq, response)
plt.title("Frequency response of Blackman window")
plt.ylabel("Magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
plt.show()