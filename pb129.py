# -------------------------------------------------------------------------------
# Name:        pb129
# Purpose:     project euler
# Created:     06/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def testa(n, lim=10**6):
    u = 1
    i = 1
    while u:
        u = (u * 10 + 1) % n
        i += 1
        if i > lim:
            return True
    return False


def main():
    start = time.perf_counter()
    test = True
    j = 10**6 - 1

    while test:
        j += 2
        if j % 5 != 0 and testa(j):
                test = False

    print(j)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())