# -------------------------------------------------------------------------------
# Name:        pb321
# Purpose:     project euler
# Created:     03/02/2016
# -------------------------------------------------------------------------------

import time
import sys


# use https://www.alpertron.com.ar/QUAD.HTM for x^2-2*y^2+x-4*y=0 beacause M(y)=y*(y+2)=x*(x+1)/2=T(x)
def solve(m):
    x1 = 2
    y1 = 1
    x2 = 5
    y2 = 3
    count = 2
    somme = 4
    while count < m:
        x1, y1 = 3*x1+4*y1+5, 2*x1+3*y1+3
        x2, y2 = 3*x2+4*y2+5, 2*x2+3*y2+3
        count += 2
        somme += y1 + y2
    return somme


def main():
    start = time.perf_counter()
    print(solve(40))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
