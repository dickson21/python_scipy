

import numpy as np 
a = np.arange(6).reshape(3,2) 

print('Our array is:') 
print(a) 
 

print('Modified array:') 
wt = np.array([3,5]) 
print(np.average(a, axis = 1, weights = wt) )
  

print('Modified array:') 
print(np.average(a, axis = 1, weights = wt, returned = True))

"""
Our array is:
[[0 1]
 [2 3]
 [4 5]]
Modified array:
[0.625 2.625 4.625]
Modified array:
(array([0.625, 2.625, 4.625]), array([8., 8., 8.]))
"""