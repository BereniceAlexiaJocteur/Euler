# -------------------------------------------------------------------------------
# Name:        pb90
# Purpose:     project euler
# Created:     15/07/2015
# -------------------------------------------------------------------------------

import itertools
import time
import sys


def extended_list(l):
    if '6' in l and '9' in l:
        return l
    elif '6' in l:
        l.append('9')
        return l
    elif '9' in l:
        l.append('6')
        return l
    else:
        return l


def test(d1, d2):
    dicotest = {}
    carres = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
    e1 = extended_list(list(d1))
    e2 = extended_list(list(d2))
    temp = True

    for k in carres:
        dicotest[k] = False

    for i in e1:
        for j in e2:
            ij = i + j
            if ij in dicotest:
                dicotest[ij] = True
            ji = j + i
            if ji in dicotest:
                dicotest[ji] = True

    for v in dicotest.values():
        if not v:
            temp = False

    return temp


def main():
    start = time.perf_counter()
    c = [item for item in itertools.combinations('0123456789', 6)]
    p = itertools.combinations(c, 2)
    resultat = 0

    for a in p:
        if test(a[0], a[1]):
            resultat += 1

    print(resultat)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())