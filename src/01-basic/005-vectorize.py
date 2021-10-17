#vectorize
import numpy as np 


def addsubtract(a,b):
   if a > b:
       return a - b
   else:
       return a + b

vec_addsubtract = np.vectorize(addsubtract)

print(vec_addsubtract([0,3,6,9],[1,3,5,7]))

"""
[1 6 1 2]
"""
