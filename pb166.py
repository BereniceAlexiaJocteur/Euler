# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

res = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                tot = a+b+c+d
                for e in range(10):
                    for i in range(10):
                        m = tot - a - e - i
                        if m not in range(10):
                            continue
                        for f in range(10):
                            for j in range(10):
                                n = tot - b - f - j
                                if n not in range(10):
                                    continue
                                for l in range(10):
                                    k = tot - i - j - l
                                    if k not in range(10):
                                        continue
                                    p = tot - a - f - k
                                    if p not in range(10):
                                        continue
                                    h = tot - d - l - p
                                    if h not in range(10):
                                        continue
                                    g = tot - e - f - h
                                    if g not in range(10):
                                        continue
                                    o = tot - c - g - k
                                    if o not in range(10):
                                        continue
                                    if m + n + o + p == tot and d + g + j + m == tot:
                                        res += 1
print(res)