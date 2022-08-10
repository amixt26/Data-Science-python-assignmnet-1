# Write a Python program to create an intersection of sets and union of sets.

Set1 = {1, 2, 3, 4, 56, 7, "sheena", "ishi"}
set2 = {1, 56, 7, "ishi", 9, 5, 8, 9, "sheena"}
set3 = {"amit", "ishi", "aloo", "sheena"}
print(Set1.intersection(set2))
print(set3.intersection(set2))
print(set2.intersection(Set1))


print(Set1.union(set2))
print(set3.union(Set1))