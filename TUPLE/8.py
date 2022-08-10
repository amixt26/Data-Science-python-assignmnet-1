# Write a Python program to remove an item from a tuple.

tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)

tuplex = tuplex[:2] + tuplex[4:]
print(tuplex)


# second way
listx = list(tuplex)
listx.remove(3)
tuplex = tuple(listx)
print(tuplex)

