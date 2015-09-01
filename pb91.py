# -------------------------------------------------------------------------------
# Name:        pb91
# Purpose:     project euler
# Created:     14/07/2015
# -------------------------------------------------------------------------------

import time
import math
import sys


def distance_au_carre(x1, y1, x2=0, y2=0):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


def main():
    start = time.perf_counter()
    resultat = 0

    for xp in range(51):
        for yp in range(51):
            op = distance_au_carre(xp, yp)
            for xq in range(51):
                for yq in range(51):
                    oq = distance_au_carre(xq, yq)
                    pq = distance_au_carre(xp, yp, xq, yq)
                    if op == oq + pq or oq == op + pq or pq == op + oq:
                        if math.sqrt(op) + math.sqrt(pq) != math.sqrt(oq) and math.sqrt(oq) + math.sqrt(
                                pq) != math.sqrt(op):
                            if (xp != 0 or yp != 0) and (xq != 0 or yq != 0):
                                resultat += 1

    print(resultat // 2)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())