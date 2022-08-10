#2. Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
num = input("Enter the comma-separated numbers: ")
list = num.split(",")
tuple = tuple(list)

print('list: ', list)
print('tuple: ', tuple)