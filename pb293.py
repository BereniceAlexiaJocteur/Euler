# -------------------------------------------------------------------------------
# Name:        pb293
# Purpose:     project euler
# Created:     01/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def build(t, p):
    temp = p
    while temp < 10**9:
        t.append(temp)
        temp *= p


def fun_fortunate(n):
    p = n + 3
    while not primes.is_prime_opti(p):
        p += 2
    return p - n


def main():
    start = time.perf_counter()
    t2 = []
    t3 = []
    t5 = []
    t7 = []
    t11 = []
    t13 = []
    t17 = []
    t19 = []
    t23 = []
    t29 = []
    build(t2, 2)
    build(t3, 3)
    build(t5, 5)
    build(t7, 7)
    build(t11, 11)
    build(t13, 13)
    build(t17, 17)
    build(t19, 19)
    build(t23, 23)
    build(t29, 29)
    admissibles = t2[:]
    pseudofortunate = set()
    resultat = 0

    for u2 in t2:
        for u3 in t3:
            tempo = u2*u3
            if tempo < 10**9:
                admissibles.append(tempo)
            else:
                break
            for u5 in t5:
                tempo = u2*u3*u5
                if tempo < 10**9:
                    admissibles.append(tempo)
                else:
                    break
                for u7 in t7:
                    tempo = u2*u3*u5*u7
                    if tempo < 10**9:
                        admissibles.append(tempo)
                    else:
                        break
                    for u11 in t11:
                        tempo = u2*u3*u5*u7*u11
                        if tempo < 10**9:
                            admissibles.append(tempo)
                        else:
                            break
                        for u13 in t13:
                            tempo = u2*u3*u5*u7*u11*u13
                            if tempo < 10**9:
                                admissibles.append(tempo)
                            else:
                                break
                            for u17 in t17:
                                tempo = u2*u3*u5*u7*u11*u13*u17
                                if tempo < 10**9:
                                    admissibles.append(tempo)
                                else:
                                    break
                                for u19 in t19:
                                    tempo = u2*u3*u5*u7*u11*u13*u17*u19
                                    if tempo < 10**9:
                                        admissibles.append(tempo)
                                    else:
                                        break
                                    for u23 in t23:
                                        tempo = u2*u3*u5*u7*u11*u13*u17*u19*u23
                                        if tempo < 10**9:
                                            admissibles.append(tempo)
                                        else:
                                            break
                                        for u29 in t29:
                                            tempo = u2*u3*u5*u7*u11*u13*u17*u19*u23*u29
                                            if tempo < 10**9:
                                                admissibles.append(tempo)
                                            else:
                                                break

    for a in admissibles:
        pseudofortunate.add(fun_fortunate(a))

    for w in pseudofortunate:
        resultat += w

    print(resultat)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())