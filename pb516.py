# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import primes
import math
import time
import sys


def bounded_products(lst, lim):
    prods = [1]
    for l in lst:
        new = []
        for k in l:
            for m in prods:
                if k*m <= lim:
                    new.append(k*m)
                else:
                    break
        prods += new
        prods.sort()
    return prods


def s(lim):
    pwrs2 = [2**k for k in range(int(math.log(lim, 2))+1)]
    pwrs3 = [3**k for k in range(int(math.log(lim, 3))+1)]
    pwrs5 = [5**k for k in range(int(math.log(lim, 5))+1)]
    hamming = [a*b*c for a in pwrs2 for b in pwrs3 for c in pwrs5 if a*b*c < lim]
    hprimes = []
    for h in hamming:
        if h+1 > 5 and primes.is_prime(h+1):
            hprimes.append([h+1])
    return sum(bounded_products([pwrs2[1:], pwrs3[1:], pwrs5[1:]]+hprimes, lim))


def main():
    start = time.perf_counter()
    print(s(10**12) % 2**32)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())