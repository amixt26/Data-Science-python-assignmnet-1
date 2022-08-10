# 3. Write a Python program to get the number of occurrences of a specified element in an array

from array import *

array = array('i', [3,4,6,7,1,10,1,5,1,3,9,5,10,4,10,1])
print('Array: ' + str(array))

print('The occurrence of 10 in array is: ')
print(array.count(10))
