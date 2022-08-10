# Write a Python program to create a set.

my_set ={1, 5, 3}  # they are placed unordered
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

# my_set = {1, 2, [3, 4]}

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

