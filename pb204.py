def primes(n):
    n += 1
    x = list(range(n))
    for i in range(2, n):
        if x[i] == i:
            x[i] = 1
            if i*i < n:
                for j in range(i*i, n, i):
                    x[j] = i
    return [i for i in range(2, n) if x[i] == 1]

print(primes(1000))