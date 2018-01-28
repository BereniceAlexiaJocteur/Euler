# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

from sympy.ntheory.modular import *
import numpy


def phi_sieve(lim):
    limit = lim + 1
    phi = numpy.empty(limit, dtype='int32')
    for i in range(limit):
        phi[i] = i
    for i in range(2, limit):
        if phi[i] == i:
            phi[i] = i - 1
            for j in range(i + i, limit, i):
                phi[j] = phi[j] // i * (i - 1)
    return phi


def solve(limmin, limmax):
    phi = phi_sieve(limmax)[limmin:limmax + 1]
    som = 0
    for n in range(limmin, limmax - 1):
        print(n)
        phin = phi[n - limmin]
        for m in range(n + 1, limmax):
            res = solve_congruence((phin, n), (phi[m - limmin], m))
            if res is not None:
                som += res[0]
    return som


print(solve(10 ** 6, 1005000))
