

import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print('Our array is:')
print(a ) 
print('\n')

print('Applying amin() function:' )
print(np.amin(a,1) ) #1:row
print('\n' ) 

print('Applying amin() function again:') 
print(np.amin(a,0) ) #0:col
print('\n')  

print('Applying amax() function:' )
print(np.amax(a)) 
print('\n' ) 

print('Applying amax() function again:')
print(np.amax(a, axis = 0))

"""
Our array is:
[[3 7 5]
 [8 4 3]
 [2 4 9]]

Applying amin() function: (each row min value)
[3 3 2]

Applying amin() function again: (each col min value)
[2 4 3]

Applying amax() function: (max. value of matrix)
9

Applying amax() function again: (max value of each column)
[8 7 9]
"""