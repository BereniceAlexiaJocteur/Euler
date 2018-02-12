# -------------------------------------------------------------------------------
# Name:        pb179
# Purpose:     project euler
# Created:     26/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    t = [0] * 10**7

    for i in range(2, 5*10**6):
        for j in range(2*i, 10**7, i):
            t[j] += 1

    print(sum(t[i] == t[i - 1] for i in range(3, 10**7)))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())