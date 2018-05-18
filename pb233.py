# -------------------------------------------------------------------------------
# Name:        pb233
# Purpose:     project euler
# Created:     09/02/2016
# -------------------------------------------------------------------------------

import primes
import time
import sys


class Problem():

    def __init__(self):
        self.primes_1mod4 = []
        self.factors_without_1mod4 = []

    def init_primes(self):
        pri = primes.primes(5*10**6)
        for i in pri:
            if i % 4 == 1:
                self.primes_1mod4.append(i)
        del pri

    def init_factors(self):
        trial = [True]*300000
        for i in self.primes_1mod4:
            if i >= 300000:
                break
            for j in range(i, 300000, i):
                trial[j] = False
        for i in range(1, len(trial)):
            if trial[i]:
                self.factors_without_1mod4.append(i)
        del trial

    def solve(self):
        self.init_primes()
        self.init_factors()
        sum = 0
        for a in range(len(self.primes_1mod4)-1):
            if self.primes_1mod4[a]**2 > 10**11:
                break
            for b in range(a+1, len(self.primes_1mod4)):
                u = self.primes_1mod4[b]**2*self.primes_1mod4[a]**10
                v = self.primes_1mod4[b]**3*self.primes_1mod4[a]**7
                if u > 10**11 and v > 10**11:
                    break
                w = self.primes_1mod4[b]**10*self.primes_1mod4[a]**2
                x = self.primes_1mod4[b]**7*self.primes_1mod4[a]**3
                for c in self.factors_without_1mod4:
                    uc = u*c
                    vc = v*c
                    if uc > 10**11 and vc > 10**11:
                        break
                    if uc <= 10**11:
                        sum += uc
                    if vc <= 10**11:
                        sum += vc
                    wc = w*c
                    if wc <= 10**11:
                        sum += wc
                    xc = x*c
                    if xc <= 10**11:
                        sum += xc
        for a in range(len(self.primes_1mod4)-2):
            for b in range(a+1, len(self.primes_1mod4)-1):
                if self.primes_1mod4[a]**2*self.primes_1mod4[b] > 10**11:
                    break
                for c in range(b+1, len(self.primes_1mod4)):
                    u = self.primes_1mod4[a]**3*self.primes_1mod4[b]**2*self.primes_1mod4[c]
                    if u > 10**11:
                        break
                    v = self.primes_1mod4[a]**3*self.primes_1mod4[b]*self.primes_1mod4[c]**2
                    w = self.primes_1mod4[a]**2*self.primes_1mod4[b]**3*self.primes_1mod4[c]
                    x = self.primes_1mod4[a]**2*self.primes_1mod4[b]*self.primes_1mod4[c]**3
                    y = self.primes_1mod4[a]*self.primes_1mod4[b]**3*self.primes_1mod4[c]**2
                    z = self.primes_1mod4[a]*self.primes_1mod4[b]**2*self.primes_1mod4[c]**3
                    for d in self.factors_without_1mod4:
                        ud = u*d
                        if ud > 10**11:
                            break
                        else:
                            sum += ud
                        vd = v*d
                        if vd <= 10**11:
                            sum += vd
                        wd = w*d
                        if wd <= 10**11:
                            sum += wd
                        xd = x*d
                        if xd <= 10**11:
                            sum += xd
                        yd = y*d
                        if yd <= 10**11:
                            sum += yd
                        zd = z*d
                        if zd <= 10**11:
                            sum += zd
        print(sum)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
