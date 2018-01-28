# -------------------------------------------------------------------------------
# Name:        pb104
# Purpose:     project euler
# Created:     17/02/2015
# -------------------------------------------------------------------------------

import math
import time
import sys


def ispan(no, s=9):
    no = str(no)
    return len(no) == s and not '1234567890'[:s].strip(no)


def main():
    start = time.perf_counter()
    test = True
    f1 = 1
    f2 = 1
    f3 = 2
    n = 2
    taille = 1000000000

    while test:
        n += 1
        f3 = f2 + f1
        queue = f3 % taille
        if ispan(queue):
            chiffres = int(math.log10(f3)) + 1
            if chiffres > 9:
                tete = f3//(10**(chiffres - 9))
                if ispan(tete):
                    test = False
        f1 = f2
        f2 = f3

    print(n)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())