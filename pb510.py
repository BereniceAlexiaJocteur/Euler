from math import *


sommee = 0
for a in range(1, 101):
    for b in range(1, a+1):
        c = (a*b)/(a+b+2*sqrt(a*b))
        if int(c) == c:
            sommee += a + b + int(c)
print(sommee)