# Write a Python program to remove an item from a set if it is present in the set.

my_set = {"ishi", "sheena", "amit", "she", "ananya" }

my_set.discard("aloo")  #If the element is not present in the set,
          # then no error or exception is raised and the original set is printed.
print(my_set)

my_set.discard("ishi")
print(my_set)