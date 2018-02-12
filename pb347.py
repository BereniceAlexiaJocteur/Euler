import time
import math


def init_prime(n):
    l = [True]*(n+1)
    prime = []
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(2*i, n+1, i):
            l[j] = False
    for i in range(2, n+1):
        if l[i]:
            prime.append(i)
    del l
    return prime


def m(p, q, n):
    curr_max = 0
    i = 1
    pi = p ** i
    while pi < n:
        j = 1
        pipj = pi*q**j
        while pipj <= n:
            if pipj > curr_max:
                curr_max = pipj
            j += 1
            pipj = pi*q**j
        i += 1
        pi = p**i
    return curr_max


def solve(n):
    pri = init_prime(n//2)
    somme = 0
    for i in range(1, len(pri)):
        p = pri[i]
        for j in range(i):
            q = pri[j]
            if p*q > n:
                break
            somme += m(p, q, n)
    return somme


start = time.perf_counter()
print(solve(10**7))
print('temps d\'exécution', time.perf_counter() - start, 'sec')