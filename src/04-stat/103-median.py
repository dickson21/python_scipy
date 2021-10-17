"""
{(n + 1) ÷ 2}th value, where n is the number of values in a set of data. 
In order to calculate the median, the data must first be ranked (sorted in ascending order). 
The median is the number in the middle. 
Median = the middle value of a set of ordered data

e.g 
[1,2,3] median = 2
[1,2,2,3,3,4,5] median = 3
"""

import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print('Our array is:' )
print(a)
 

print('Applying median() function:' )
print(np.median(a)) 
  

print('Applying median() function along axis 0:' )
print(np.median(a, axis = 0) ) 
 
print('Applying median() function along axis 1:' )
print(np.median(a, axis = 1))

"""
Our array is:
[[30 65 70]
 [80 95 10]
 [50 90 60]]
Applying median() function:
65.0
Applying median() function along axis 0:
[50. 90. 60.]
Applying median() function along axis 1:
[65. 80. 60.]
"""