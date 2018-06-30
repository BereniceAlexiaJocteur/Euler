import time
import sys
import math

"""I solved this problem using http://www.personal.psu.edu/jxs23/p7.pdf and 
http://mathworld.wolfram.com/SumofSquaresFunction.html"""


class Problem():

    @staticmethod
    def r2(n):  # returns numbers of ways of writing n as a sum of two positive squares
        B = 1
        while n % 2 == 0:
            n //= 2
        p = 3
        while n > 1 and p**2 <= n:
            coeff_de_p = 0
            while n % p == 0:
                coeff_de_p += 1
                n //= p
            if coeff_de_p % 2 != 0:
                return 0
            p += 2
            if n == 1 or p**2 > n:
                break
            coeff_de_p = 0
            while n % p == 0:
                coeff_de_p += 1
                n //= p
            B = B*(coeff_de_p + 1)
            p += 2
        if n > 1:  # n est nécessairement premier
            if n % 4 == 3:
                return 0
            else:
                B *= 2
        return B

    def r3_brute(self, n): # returns numbers of ways of writing n as a sum of three positive squares
        res = 0
        for i in range(1, int(math.sqrt(n))+1):
            res += self.r2(n-i*i)
        return res

    def r3_opti(self, n):
        lamb = 0
        while n % 9 == 0:
            lamb += 1
            n //= 9
        if lamb > 0:
            if n % 24 == 11:
                return 3**lamb*self.r3_opti(n)
            if n % 24 == 19:
                return (2*3**lamb-1)*self.r3_opti(n)
            if n % 72 == 3 or n % 72 == 51:
                return ((3**(lamb+1)-1)//2)*self.r3_opti(n)
        n = n * 9**lamb
        return self.r3_brute(n)

    def G(self, n):
        if n % 27 == 12:
            u = n // 27
            return 3*self.G(3*u+1)
        if n % 27 == 21:
            u = n // 27
            return 5*self.G(3*u+2)
        if n % 81 == 3:
            u = n // 81
            return 4*self.G(9*u)
        if n % 81 == 57:
            u = n // 81
            return 4*self.G(9*u+6)
        else:
            return self.r3_opti(8*n+3)

    def solve(self):
        print(self.G(17526*10**9))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
