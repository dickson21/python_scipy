"""
Weighted average is an average resulting from the multiplication of each component by a factor reflecting its importance. The numpy.average() function computes the weighted average of elements in an array according to their respective weight given in another array. The function can have an axis parameter. If the axis is not specified, the array is flattened.

Considering an array [1,2,3,4] and corresponding weights [4,3,2,1], the weighted average is calculated by adding the product of the corresponding elements and dividing the sum by the sum of weights.

Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)
"""

import numpy as np 
a = np.array([1,2,3,4]) 

print('Our array is:' )
print(a )

print('Applying average() function:') 
print(np.average(a) )

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,1]) 

print('Applying average() function again:' )
print(np.average(a,weights = wts)) 
 

# Returns the sum of weights, if the returned parameter is set to True. 
print 'Sum of weights' 
print np.average([1,2,3, 4],weights = [4,3,2,1], returned = True)