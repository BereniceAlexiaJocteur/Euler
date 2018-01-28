# -------------------------------------------------------------------------------
# Name:        pb455
# Purpose:     project euler
# Created:     02/02/2016
# -------------------------------------------------------------------------------


def solve(n):
    somme = 0
    for i in range(2, n+1):
        a = 0
        b = i
        while b != a and b:
            c = a
            a = b
            b = pow(i, c, 10**9)
        somme += b
    return somme

print(solve(10**6))
