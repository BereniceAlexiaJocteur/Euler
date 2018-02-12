# -------------------------------------------------------------------------------
# Name:        pb500
# Purpose:     project euler
# Created:     16/07/2015
# -------------------------------------------------------------------------------

import math
import primes
import heapq
import time
import sys


start = time.perf_counter()


# I use Rosser's theorem to find an upperbound for the nth prime
def upper_bound_prime(n):
    return int(n * (math.log(n) + math.log(math.log(n))))


def main():
    # I generate a sieve (with erastophene) of the 500500 first primes, actually a bit more beacause the upper bound is
    # not really accurate
    sieve = primes.primes(upper_bound_prime(500500))
    # the length of sieve is initially 530758 so I restrict its length to  500500
    sieve = sieve[:500500]
    # I want to generate a list which is a copy sieve where I add the powers of the form : "element of sieve"^2
    # But when for a element of sieve this item is greater than the last element of the sieve I will do the same with
    # the formula "element of sieve"^4 until I reach the same limit then with "element"^8 and so on
    # finally I will take the 500500 smallest items of this list and multiply them
    # This number is the smallest with 2^500500 divisors
    # Indeed the sum of the powers of the prime factors of a number with 2^n divisors is n
    # And since I have choosen the smallest prime powers it is indeed the smallest number with 2^n divisors
    limit = sieve[-1]
    i = 0
    j = 2
    test = True
    resultat = 1

    while test:
        while sieve[i]**j < limit:
            sieve.append(sieve[i]**j)
            i += 1
        j *= 2
        if i == 0:
            test = False
        i = 0
    # Now I will take the 500500 smallest elements of sieve
    t = heapq.nsmallest(500500, sieve)
    # And finally I make the product modulo 500500507 of all the elements in t
    for k in t:
        resultat = (resultat * k) % 500500507

    print(resultat)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())