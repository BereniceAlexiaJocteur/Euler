# -------------------------------------------------------------------------------
# Name:        pb62
# Purpose:     project euler
# Created:     11/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def ordonnemot(s):
    temp = sorted(s)
    w = ''
    for x in range(0, len(temp)):
        w += temp[x]
    return w


def main():
    start = time.perf_counter()
    test = True
    i = 1
    tableau = []

    while test:
        u = i ** 3
        v = ordonnemot(str(u))
        temp1 = True
        j = 0
        while temp1 and j < len(tableau):
            if tableau[j][0] == v:
                tableau[j][1] += 1
                temp1 = False
                if tableau[j][1] == 5:
                    test = False
                    print(tableau[j][2])
                    break
            j += 1
        if temp1 is True:
            tableau.append([v, 1, u])
        i += 1

    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())