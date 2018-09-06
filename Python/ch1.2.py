import math

def reverse(str):
    for i in range(0, math.floor(len(str)/2)):
        endi = len(str) - i - 1
        tmp = str[i]
        str[i] = str[endi]
        str[endi] = tmp

str = bytearray('hello'.encode())
reverse(str)
print(str)
