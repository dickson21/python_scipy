
"""
Subject : Matrix inverse, transpose, multiply
Status : OK
Detail : 
Despite its convenience, the use of the numpy.matrix class is discouraged, 
since it adds nothing that cannot be accomplished with 2D numpy.ndarray objects, 
and may lead to a confusion of which class is being used. 
For example, the above code can be rewritten as:

"""

import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
print(A)
"""
array([[1, 2],
      [3, 4]])
"""
linalg.inv(A)
"""
array([[-2. ,  1. ],
      [ 1.5, -0.5]])
"""
b = np.array([[5,6]]) #2D array
print(b)
# array([[5, 6]])
print(b.T)
"""
array([[5],
      [6]])
"""
print(A*b) #not matrix multiplication!
"""
array([[ 5, 12],
      [15, 24]])
"""
print(A.dot(b.T)) #matrix multiplication
"""
array([[17],
      [39]])
"""
b = np.array([5,6]) #1D array
print(b)
#array([5, 6])
print(b.T)  #not matrix transpose!
"""
array([5, 6])
"""
print(A.dot(b))  #does not matter for multiplication
# array([17, 39])