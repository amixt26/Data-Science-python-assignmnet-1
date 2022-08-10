# Write a Python program to use of frozenset.

my_set = {"amit", 10, "annu", "A"}    # frozenset are immutable ie cant be modify

fset = frozenset(my_set)

print(fset)

# fset.remove("A")    frozenset doesnt have remove attribute so it will show error