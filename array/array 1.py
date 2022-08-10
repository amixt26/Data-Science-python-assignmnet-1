# Write a Python program to create an array of 5 integers and display the array items.Access individual element through indexes.

from array import *
array_num = array('i', [3,9,4,10,15])
for i in array_num:
          print(i)
print('Access individual element: ')
print(array_num[-1])
print(array_num[3])
print(array_num[0])


