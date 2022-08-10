# Write a Python program to create set of symmetric difference.

A = { "APPLE", "BALL", "CAT", "DOG", "ELEPHANT"}
B = { "AMIT", "KAVERI", "CAT", "BALL", "MIA"}

print(A.symmetric_difference(B))               # Original sets:
                                               # {'blue', 'green'}
                                               # {'yellow', 'blue'}

                                               # Symmetric difference of setc1 - setc2:
                                               # {'yellow', 'green'}

print(B.symmetric_difference(A))