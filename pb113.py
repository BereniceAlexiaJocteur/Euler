# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import math
import time
import sys


def binomial(x, y):
    if y == x:
        return 1
    elif y == 1:
        return x
    elif y > x:
        return 0
    else:
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x-y)
        div = a // (b * c)
        return div


def main():
    start = time.perf_counter()
    resultat = binomial(110, 10) + binomial(109, 9) - 1002

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())