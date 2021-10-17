"""
subject : polynomial

"""
import numpy as np 
from numpy import poly1d
from matplotlib import pyplot as plt

p = poly1d([3,4,5]) # p = 3x^2 + 4x + 5
print(p)
print(p(1))  #x=1 p=3 + 4 + 5 = 12
print(p*p) #9x^4 + 24x^3 + 46x^2 + 40x + 25
y = p*p
print(y(1))

a = p.integ(k=6)
print(a) # integral p = 1x^3 + 2x^2 + 5x + 6

print(a.deriv()) # 3x^2 + 4x + 5

print(p.deriv()) # 6x + 4
print(p([4, 5])) # array[69,100]

x = np.arange(0,4)
print(x)
y = p(x)
print(y)

plt.title("3x^2 + 4x + 5")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()



"""
   2
3 x + 4 x + 5
12
   4      3      2
9 x + 24 x + 46 x + 40 x + 25
144
   3     2
1 x + 2 x + 5 x + 6
   2
3 x + 4 x + 5

6 x + 4
[ 69 100]
[0 1 2 3]
[ 5 12 25 44]
"""

