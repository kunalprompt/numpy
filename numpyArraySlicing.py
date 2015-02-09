'''
Hello World!
http://kunalprompt.github.io
'''

print __doc__

import numpy as np

'''
Indexing, and Slicing in Python Numpy

There are three kinds of indexing available: 
1. record access, 
2. basic slicing, 
3. advanced indexing
Which one occurs depends on obj.
'''

# Record Access already done.

# Slicing (start:stop:step)

# 1D Slicing
numObjA = np.arange(20, dtype='float')
print "1-D numObjA Slicing "
# like an array, indexing goes here as
# array = 112 12 133
# Indexes = 0  1  2
# Indexing= -3 -2 -1
start=13;stop=17;step=1 # [::-1] to reverse the ndarray
print numObjA[start:stop: step]

# 2D Slicing
numObjB = np.reshape(np.arange(20, dtype='float'), (5,4))
print "numObjB \n", numObjB
print "Slicing the 2-D numpy object numObjB "
print numObjB[1:3, 0:2] # like numObj[0:5, 1:2] will return all rows (start=1, stop=5, step=1) and colums (start=1, stop=2, step=1)