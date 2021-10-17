

"""
plot sin wave
https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html

"""

# Make plots appear inline, set custom plotting style
#matplotlib inline
import matplotlib.pyplot as plt
#plt.style.use('style/elegant.mplstyle')
import numpy as np 
f = 10  # Frequency, in cycles per second, or Hertz
f_s = 100  # Sampling rate, or number of measurements per second

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(f * 2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Signal amplitude')
#plt.subplot(2,1,1)
plt.show()




