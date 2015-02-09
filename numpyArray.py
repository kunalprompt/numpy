'''
Hello World!
http://kunalprompt.github.io

Introduction to NumPy Objects
'''
print __doc__

from numpy import *

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print "This a Python List of Lists - \n", lst
print "Converting this to NumPy Object..."


# creating a numpy object (ie. a multidimensional array)
num_obj = array(lst)
print num_obj
print "Type of Numpy Object - "+str(type(num_obj))
print "Number of dimensions or axes this object has are - "+str(num_obj.ndim)
print "Data Type of this object - "+str(num_obj.dtype)

x=2;y=1
print "Value of element at %d, %d of this numpy object is -"%(x, y), num_obj[x, y]