"""
Combinatorics
comb(N, k[, exact, repetition])
The number of combinations of N things taken k at a time.

perm(N, k[, exact])
Permutations of N things taken k at a time, i.e., k-permutations of N.

Ref:
combination
https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html#scipy.special.comb

permutation
https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.perm.html

facforial
https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.factorial.html#scipy.special.factorial

Example
from scipy.special import comb
k = np.array([3, 4])
n = np.array([10, 10])
comb(n, k, exact=False)
array([ 120.,  210.])
comb(10, 3, exact=True)
120
comb(10, 3, exact=True, repetition=True)
220
"""

import numpy as np 
from scipy.special import comb
from scipy.special import perm
from scipy.special import factorial

k = np.array([3, 4])
n = np.array([10, 10])
print(comb(n, k, exact=False))
print(comb(10, 3, exact=True))
print(comb(10, 3, exact=True, repetition=True))

k = np.array([2])
n = np.array([3])
print("Combination")
print(comb(n, k, exact=False, repetition=False)) #n!/(k!(n-k)!) = 3!/(2!(3-2)!)
print(comb(n, k, exact=False, repetition=True)) #n!/(k!(n-k)!) = 3!/(2!(3-2)!)

print("Permutation")
print(perm(n,k))
print(perm(n,k, exact=False))
# print(perm(n,k, exact=True)) 
# #TypeError: only integer scalar arrays can be converted to a scalar index

print("Factorial")
arr = np.array([3, 4, 5])
result = factorial(arr, exact=False)
print(result)

"""
[120. 210.]
120
220
Combination
[3.]
[6.]
Permutation
[6.]
[6.]
Factorial
[  6.  24. 120.]
"""





