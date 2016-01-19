# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import primes

p = primes.primes(10**6)
l = len(p)
res = 11

for a1 in range(1, l):
    p1 = p[a1]
    p1p = p1 - 1
    for a2 in range(a1+1, l, 1):
        p2 = p[a2]
        n2 = p1*p2
        if n2 > 10**12:
            break
        n2p = n2+3
        p2p = p2 - 1
        if n2p % p1p == 0 and n2p % p2p == 0:
            res += n2
        for a3 in range(a2+1, l, 1):
            p3 = p[a3]
            n3 = n2*p3
            if n3 > 10**12:
                break
            p3p = p3 - 1
            n3p = n3 + 3
            if n3p % p1p == 0 and n3p % p2p == 0 and n3p % p3p == 0:
                res += n3
            for a4 in range(a3+1, l, 1):
                p4 = p[a4]
                n4 = n3*p4
                if n4 > 10**12:
                    break
                p4p = p4 - 1
                n4p = n4 + 3
                if n4p % p1p == 0 and n4p % p2p == 0 and n4p % p3p == 0 and n4p % p4p == 0:
                    res += n4
                for a5 in range(a4+1, l, 1):
                    p5 = p[a5]
                    n5 = n4*p5
                    if n5 > 10**12:
                        break
                    p5p = p5 - 1
                    n5p = n5 + 3
                    if n5p % p1p == 0 and n5p % p2p == 0 and n5p % p3p == 0 and n5p % p4p == 0 and n5p % p5p == 0:
                        res += n5
                    for a6 in range(a5+1, l, 1):
                        p6 = p[a6]
                        n6 = n5*p6
                        if n6 > 10**12:
                            break
                        p6p = p6 - 1
                        n6p = n6 + 3
                        if n6p % p1p == 0 and n6p % p2p == 0 and n6p % p3p == 0 and n6p % p4p == 0 and n6p % p5p == 0 and n6p % p6p == 0:
                            res += n6
                        for a7 in range(a6+1, l, 1):
                            p7 = p[a7]
                            n7 = n6*p7
                            if n7 > 10**12:
                                break
                            p7p = p7 - 1
                            n7p = n7 + 3
                            if n7p % p1p == 0 and n7p % p2p == 0 and n7p % p3p == 0 and n7p % p4p == 0 and n7p % p5p == 0 and n7p % p6p == 0 and n7p % p7p == 0:
                                res += n7
                            for a8 in range(a7+1, l, 1):
                                p8 = p[a8]
                                n8 = n7*p8
                                if n7 > 10**12:
                                    break
                                p8p = p8 - 1
                                n8p = n8 + 3
                                if n8p % p1p == 0 and n8p % p2p == 0 and n8p % p3p == 0 and n8p % p4p == 0 and n8p % p5p == 0 and n8p % p6p == 0 and n8p % p7p == 0 and n8p % p8p == 0:
                                    res += n8
                                for a9 in range(a8+1, l, 1):
                                    p9 = p[a9]
                                    n9 = n8*p9
                                    if n9 > 10**12:
                                        break
                                    p9p = p9 - 1
                                    n9p = n9 + 3
                                    if n9p % p1p == 0 and n9p % p2p == 0 and n9p % p3p == 0 and n9p % p4p == 0 and n9p % p5p == 0 and n9p % p6p == 0 and n9p % p7p == 0 and n9p % p8p == 0 and n9p % p9p == 0:
                                        res += n9
                                    for a10 in range(a9+1, l, 1):
                                        p10 = p[a10]
                                        n10 = n9*p10
                                        if n10 > 10**12:
                                            break
                                        p10p = p10 - 1
                                        n10p = n10 + 3
                                        if n10p % p1p == 0 and n10p % p2p == 0 and n10p % p3p == 0 and n10p % p4p == 0 and n10p % p5p == 0 and n10p % p6p == 0 and n10p % p7p == 0 and n10p % p8p == 0 and n10p % p9p == 0 and n10p % p10p == 0:
                                            res += n10
                                        for a11 in range(a10+1, l, 1):
                                            p11 = p[a11]
                                            n11 = n10*p11
                                            if n11 > 10**12:
                                                break
                                            p11p = p11 - 1
                                            n11p = n11 + 3
                                            if n11p % p1p == 0 and n11p % p2p == 0 and n11p % p3p == 0 and n11p % p4p == 0 and n11p % p5p == 0 and n11p % p6p == 0 and n11p % p7p == 0 and n11p % p8p == 0 and n11p % p9p == 0 and n11p % p10p == 0 and n11p % p11p == 0:
                                                res += n11


print(res)