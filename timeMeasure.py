'''
Hello World!
http://kunalprompt.github.io

How much time it takes for a code to finish execution?
'''
import time
start_time = time.time()

# Print the factorial of 200
fact=1
for i in range(2, 201):
	fact*=i

print fact
end_time = time.time()
print "[Finished in "+str(float(end_time-start_time))+"]"

'''
A linux time utility

$ time python timeMeasure.py
'''