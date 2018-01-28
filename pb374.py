# -------------------------------------------------------------------------------
# Name:        pb374
# Purpose:     project euler
# Created:     30/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    start = time.perf_counter()
    inv2 = mul_inv(2, 982451653)
    somme1 = 3
    fact1 = 1
    fact2 = 2
    inv = 0
    inv1 = 0

    for m in range(2, 14142136):
        fact1, fact2 = fact2, (fact2 * (m+1)) % 982451653
        inv = (inv + mul_inv(m, 982451653)) % 982451653
        if m == 12392314:
            inv1 = inv
        somme1 += (m-1)*(fact2 * inv + fact1 * (m+2) * inv2) + fact2 * m

    somme2 = fact2 * (inv1 * (14142135-1) + 14142135) + fact1 * (14142135+2) * (14142135-1) * inv2
    somme1 -= somme2

    print(somme1 % 982451653)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())