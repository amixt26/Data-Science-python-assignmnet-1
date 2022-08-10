# Write a Python program to remove the first occurrence of a specified element from an array

from array import *

array_values = array('i', [1, 2 , 3, 4, 5, 6, 1, 2, 3, 4, 56, 10, 9, 10, 1, 15])
print(array_values)

print('New array: ')
array_values.remove(56)
print(array_values)