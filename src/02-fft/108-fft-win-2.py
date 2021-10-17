"""
Subject : blackman window
Status : OK

ref:
blackman window
https://numpy.org/doc/stable/reference/generated/numpy.blackman.html

"""

import numpy as np 
from numpy.fft import fft, fftshift
import matplotlib.pyplot as plt

window = np.blackman(51)
plt.plot(window)

plt.title("Blackman window")
#Text(0.5, 1.0, 'Blackman window')
plt.ylabel("Amplitude")
#Text(0, 0.5, 'Amplitude')
plt.xlabel("Sample")
#Text(0.5, 0, 'Sample')
plt.show()