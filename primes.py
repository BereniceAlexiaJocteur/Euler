import numpy
import math


def sieve(n):
    b, p, ps = [True] * (n + 1), 2, []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in range(p, n + 1, p):
                b[i] = False
    return ps


def primes(n):
    if type(n) != int:
        raise TypeError('must be integer')
    if n < 2:
        raise ValueError('must be greater than one')
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:
            ps.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1
        p += 2
    del b
    return ps


def td_prime(n, limit=1000000):
    if type(n) != int:
        raise TypeError('must be integer')
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if limit < d:
            raise OverflowError('limit exceeded')
        if n % d == 0:
            return False
        d += 2
    return True


def td_factors(n, limit=1000000):
    if type(n) != int:
        raise TypeError('must be integer')
    fs = []
    while n % 2 == 0:
        fs += [2]
        n /= 2
    if n == 1:
        return fs
    f = 3
    while f * f <= n:
        if limit < f:
            raise OverflowError('limit exceeded')
        if n % f == 0:
            fs += [f]
            n /= f
        else:
            f += 2
    return fs + [int(n)]


def is_prime(n):
    if type(n) != int:
        raise TypeError('must be integer')
    if n < 2:
        return False
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_spsp(n, a):
        d, s = n - 1, 0
        while d % 2 == 0:
            d /= 2
            s += 1
        t = pow(a, int(d), n)
        if t == 1:
            return True
        while s > 0:
            if t == n - 1:
                return True
            t = (t * t) % n
            s -= 1
        return False

    if n in ps:
        return True
    for p in ps:
        if not is_spsp(n, p):
            return False
    return True


def rho_factors(n, limit=1000000):
    if type(n) != int:
        raise TypeError('must be integer')

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def rho_factor(n, c, limit):

        def f(x):
            return (x * x + c) % n

        t, h, d = 2, 2, 1
        while d == 1:
            if limit == 0:
                raise OverflowError('limit exceeded')
            t = f(t)
            h = f(f(h))
            d = gcd(t - h, n)
        if d == n:
            return rho_factor(n, c + 1, limit)
        if is_prime(int(d)):
            return d
        return rho_factor(d, c + 1, limit)

    if -1 <= n <= 1:
        return [n]
    if n < -1:
        return [-1] + rho_factors(-n, limit)
    fs = []
    while n % 2 == 0:
        n //= 2
        fs = fs + [2]
    if n == 1:
        return fs
    while not is_prime(int(n)):
        f = rho_factor(n, 1, limit)
        n = n / f
        fs = fs + [int(f)]
    return sorted(fs + [int(n)])


def sieve8(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p*p//3::2*p] = False
            prime[p*(p-2*(i & 1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2, result]


def is_prime_opti(n):
    """
  http://mathworld.wolfram.com/StrongPseudoprime.html
  Zhang (2001, 2002, 2005, 2006, 2007) conjectured that
  """
    firstPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139]
    lpow = pow
    if n >= 10 ** 36:
        # w = range(2, int(2*log(n)**2)) # pour etre deterministe, ERH dependent !!!
        # (log 2)-1 log n log log n.
        logn = math.log(n)
        w = range(2, int(logn * math.log(logn) / math.log(2)))  # meilleure borne, conjecture !!!

    elif n >= 1543267864443420616877677640751301:
        w = firstPrime[:20]
    # elif n >= 1543267864443420616877677640751301: w = firstPrime[:19]
    elif n >= 564132928021909221014087501701:
        w = firstPrime[:18]
    # elif n >= 564132928021909221014087501701: w = firstPrime[:17]
    elif n >= 59276361075595573263446330101:
        w = firstPrime[:16]
    elif n >= 6003094289670105800312596501:
        w = firstPrime[:15]
    elif n >= 3317044064679887385961981:
        w = firstPrime[:14]
    elif n >= 318665857834031151167461:
        w = firstPrime[:13]
    elif n >= 3825123056546413051:
        w = firstPrime[:12]  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n >= 341550071728321:
        w = firstPrime[:9]  # [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n >= 3474749660383:
        w = firstPrime[:7]  # [2, 3, 5, 7, 11, 13, 17]
    elif n >= 2152302898749:
        w = firstPrime[:6]  # [2, 3, 5, 7, 11, 13]
    elif n >= 4759123141:
        w = firstPrime[:5]  # [2, 3, 5, 7, 11]
    elif n >= 9006403:
        w = [2, 7, 61]
    elif n >= 489997:
        if n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 \
                and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and n % 47 \
                and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73 and n % 79 \
                and n % 83 and n % 89 and n % 97 and n % 101:
            # Fermat 2, 3, 5, special remix
            hn = n >> 1
            nm1 = n - 1
            p = lpow(2, hn, n)
            if p == 1 or p == nm1:
                p = lpow(3, hn, n)
                if p == 1 or p == nm1:
                    p = lpow(5, hn, n)
                    return p == 1 or p == nm1
        return False
    elif n >= 42799:
        # Fermat 2, 5
        return (n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19
                and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and lpow(2, n - 1, n) == 1
                and lpow(5, n - 1, n) == 1)
    elif n >= 841:
        # Fermat 2
        return (n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17
                and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43
                and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73
                and n % 79 and n % 83 and n % 89 and n % 97 and n % 101 and n % 103
                and lpow(2, n - 1, n) == 1)
    elif n >= 25:
        # divisions seules
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 and n % 23
    elif n >= 4:
        return n & 1 and n % 3
    else:
        return n > 1

    if not (n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17
            and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43
            and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73
            and n % 79 and n % 83 and n % 89):
        return False

    # Miller-Rabin, avec témoins "w"
    s = 0
    d = n - 1
    while not d & 1:
        d >>= 1
        s += 1
    for p in w:
        x = lpow(p, d, n)
        if x == 1:
            continue
        for _ in range(s):
            if x + 1 == n:
                break
            x = x * x % n
        else:
            return False
    return True


def upper_bound_prime(n):
    return int(n * (math.log(n) + math.log(math.log(n))))


def sieve_seg(N):
    n = int(N**0.5)
    p = list(range(n+1))
    for j in range(2, n+1):
        if p[j]:
            for k in range(j**2, n+1, j):
                    p[k] = False
    P = [l for l in p[2:] if l]
    m = 1
    while (m+1)*n < N:
        u = (m+1)*n+1
        p = list(range(m*n+1, u))
        for x in P:
            v = x*((m*n)//x+1)
            if v > u:
                break
            for y in range(v, u, x):
                p[y-m*n-1] = False
        for j in range(len(p)):
            if p[j]:
                if p[j] > n**0.5+m*n+1:
                    break
                for k in range(p[j]**2, p[-1]+1, p[j]):
                    p[k] = False
        P += [l for l in p if l]
        m += 1
    p = list(range(m*n+1, N+1))
    for x in P:
        v = x*((m*n)//x+1)
        if v > N and v/x*(x-1) > m*n+1:
            v = v//x*(x-1)
        for y in range(v, N+1, x):
            p[y-m*n-1] = False
    for j in range(len(p)):
            if p[j]:
                if p[j] > n**0.5+m*n+1:
                    break
                for k in range(p[j]**2, p[-1]+1, p[j]):
                    p[k] = False
    P += [l for l in p if l]
    return P