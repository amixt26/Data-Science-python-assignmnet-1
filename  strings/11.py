# Write a Python program to reverse a string.

def reverse(str):
    str1 = []
    for i in str:
        str1 = i + str1
    return str1

str = "AMIT PANDEY"

print("The reversed string(using loops) is : ", end="")
print(reverse(str))
