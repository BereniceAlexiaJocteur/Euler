# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import itertools


def f(seq):
    u = list(seq)
    t = sorted(u)
    np_steps = 0
    while u != t:
        for j in range(len(u) - 1):
            if u[j] > u[j+1]:
                temp = u[j+1]
                del u[j+1]
                u.insert(0, temp)
                np_steps += 1
                break
    return np_steps

compt = 0
expct = 0
for i in itertools.permutations(range(1, 20)):
    compt += 1
    expct += f(list(i))
    print(expct / compt)
print(expct / compt)

