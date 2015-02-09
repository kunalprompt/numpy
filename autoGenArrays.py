'''
Hello World!
http://kunalprompt.github.io
'''
print (__doc__)
import numpy

start=9;stop=22;step=2

print "Auto generating a 1-D numpy object"
num_objA = numpy.arange(start, stop, step, 'float')
#arange(start, stop, step, dtype)
print num_objA

print "Auto generating a Multi-D numpy object"
num_objB = numpy.reshape(numpy.arange(6, 66),(5,3,4))
# reshape(<ndarray>, <dimensions>)
# here 3*4 indicates a array of 3 rows and 4 columns
# and then 5 such such 3*4 ndarrays
print num_objB