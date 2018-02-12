import time


# return the number of divisors for every numbers <= n in a list
def sieve_number_of_divisors(n):
    l = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            l[j] += 1
    print('ok')
    return l


# return the number of each T(i) for i<=n in a list
def number_of_divisors_of_triangle_numbers(n):
    T = [0]*(n+1)
    l = sieve_number_of_divisors(n+1)
    for i in range(1, n+1, 2):
        T[i] = l[i]*l[i//2+1]
    for i in range(2, n+1, 2):
        T[i] = l[i//2]*l[i+1]
    del l
    print('ok')
    return T


def number_of_increasing_substrings_of_l_of_length_k(l, k):
    n = len(l)
    m = max(l)
    dp = []
    sol = 0
    for i in range(n+2):
        dp.append([])
        for j in range(k-1):
            dp[i].append(0)
    for p in range(0, k-1):
        num = [0]*(m+1)
        for i in range(2, n+1):
            print(i)
            if p == 0:
                num[l[i-2]] += 1
            else:
                num[l[i-2]] += dp[i-1][p-1]
            for j in range(1, l[i-1]):
                dp[i][p] += num[j]
    for i in range(n+1):
        sol = (sol + dp[i][k-2]) % 10**18
    return sol


def solve(n):
    return number_of_increasing_substrings_of_l_of_length_k(list(reversed(number_of_divisors_of_triangle_numbers(n))), 3)


start = time.perf_counter()
print(solve(6*10**7))
print('temps d\'exécution', time.perf_counter() - start, 'sec')
