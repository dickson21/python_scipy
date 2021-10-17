
"""
Subject : Matrix inverse, transpose, multiply
Status : OK
"""

import numpy as np
A = np.mat('[1 2;3 4]')
print(A)
"""
matrix([[1, 2],
        [3, 4]])
"""
print(A.I)
"""
matrix([[-2. ,  1. ],
        [ 1.5, -0.5]])
"""
b = np.mat('[5 6]')
print(b)
#matrix([[5, 6]])
print(b.T)
""""
matrix([[5],
        [6]])
"""
print(A*b.T)
"""
matrix([[17],
        [39]])
"""