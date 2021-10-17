

import numpy as np 
import matplotlib.pyplot as plt
from scipy import fftpack

#x = np.zeros(500)
#x[100:150] = 1
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

X = fftpack.fft(x)
print(np.abs(X))

f, (ax0, ax1) = plt.subplots(2, 1, sharex=True)

ax0.plot(x)
ax0.set_ylim(-1.5, 2.5)
ax0.grid(True)

ax1.plot(fftpack.fftshift(np.abs(X)))
ax1.set_ylim(0, 6)
ax1.grid(True)
#plt.grid()
plt.show()

"""
fft = np.abs(X)
[4.5        2.65688107 2.43741318 2.43741318 2.65688107]
"""