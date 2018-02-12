# -------------------------------------------------------------------------------
# Name:        pb267
# Purpose:     project euler
# Created:     24/08/2015
# -------------------------------------------------------------------------------

import eulerfun
import time
import sys


def main():
    start = time.perf_counter()
    res = 0

    for i in range(0, 432):
        res += eulerfun.binomial(1000, i)

    print(round((1-res/2**1000), 12))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())