# Write a Python program to reverse a tuple.

def Reverse(tuplex):
    new_t = tuplex[::-1]
    return new_t



tuplex = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
print(Reverse(tuplex))