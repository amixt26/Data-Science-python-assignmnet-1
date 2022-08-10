# 3. Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def replace_first_ch(str):
    ch = str[0]
    str = str.replace(ch, '$')
    str = ch + str[1:]  # exclude the ch
    return str
print(replace_first_ch('amita'))


# a=[1,5,9,11,2,66]
#
# print(a[:4])