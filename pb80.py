from math import *


def sumdigits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

result = 0
j = 1
 
for i in range(1, 101):
    if j * j == i:
        j += 1
        continue
    result += sumdigits(sqrt(i))

print(result)
