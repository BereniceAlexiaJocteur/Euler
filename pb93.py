# -------------------------------------------------------------------------------
# Name:        pb93
# Purpose:     project euler
# Created:     14/07/2015
# -------------------------------------------------------------------------------

import operator
import itertools
import time
import sys


def fonction(s):
    l = sorted(list(s))
    i = 0
    while l[i] < 1:
        i += 1
    j = 1
    while l[i] == j:
        i += 1
        j += 1
    return j - 1


def main():
    start = time.perf_counter()
    maximum = 28
    sol = {1, 2, 3, 4}

    for terms in itertools.combinations(range(1, 10), 4):
        t = set()
        for n in itertools.permutations(terms):
            for o1 in [operator.add, operator.sub, operator.mul, operator.truediv]:
                for o2 in [operator.add, operator.sub, operator.mul, operator.truediv]:
                    for o3 in [operator.add, operator.sub, operator.mul, operator.truediv]:
                        if o1 != operator.truediv or o3(n[2], n[3]) != 0:
                            u = o1(o2(n[0], n[1]), o3(n[2], n[3]))
                            if u == int(u):
                                t.add(int(u))
                        if o2 != operator.truediv or o3(n[0], n[1]) != 0:
                            if o1 != operator.truediv or o2(o3(n[0], n[1]), n[2]) != 0:
                                u = o1(o2(o3(n[0], n[1]), n[2]), n[3])
                                if u == int(u):
                                    t.add(int(u))
        if fonction(t) > maximum:
            maximum = fonction(t)
            sol = terms

    print(sol)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())