# -------------------------------------------------------------------------------
# Name:        pb134
# Purpose:     project euler
# Created:     28/07/2015
# -------------------------------------------------------------------------------

# Tres long autour de 10 heures !!

import primes
import sys


def main():
    p = primes.primes(1000008)
    compteur = 0

    for i in range(2, len(p)-1):
        p1 = p[i]
        p2 = p[i+1]
        k = 1
        u = str(k)+str(p1)
        while int(u) % p2 != 0:
            k += 1
            u = str(k)+str(p1)
        compteur += int(u)

    print(compteur)

if __name__ == '__main__':
    sys.exit(main())