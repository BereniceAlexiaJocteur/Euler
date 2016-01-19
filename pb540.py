# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------
import math
import fractions


def fonction(n):
    ctr = 0
    for i in range(1, int(math.sqrt(2*n/(1+(1+math.sqrt(2))**2)))+1):
        print(i)
        if i % 2 == 1:
            n1 = int(i/math.sqrt(2))+1
            nv = int((math.sqrt(2*n-i**2)-i)/2)
            for j in range(n1, nv+1):
                if fractions.gcd(i, j) == 1:
                    ctr += 1
    for i in range(1, int(math.sqrt(n/(1+(1+math.sqrt(2))**2)))+1):
        n1 = int(i*math.sqrt(2))+1
        nv = int(math.sqrt(n-i**2)-i)
        for j in range(n1, nv+1):
            if j % 2 == 1:
                if fractions.gcd(i, j) == 1:
                    ctr += 1
    return ctr

print(fonction(3141592653589793))