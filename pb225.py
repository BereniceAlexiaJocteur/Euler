# -------------------------------------------------------------------------------
# Name:        pb225
# Purpose:     project euler
# Created:     27/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    t = [1] * 13000
    compteur = 1
    div = 27

    for i in range(3, 13000):
        t[i] = t[i-3] + t[i-2] + t[i-1]

    while compteur < 127:
        div += 2
        finddiv = False
        for k in t:
            if k % div == 0:
                finddiv = True
                break
        if not finddiv:
            compteur += 1

    print(div)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())