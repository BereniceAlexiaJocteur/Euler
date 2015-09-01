# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    scores_on_1_hit = [25, 50]
    scores_double = [50]
    compteur = 0

    for a in range(1, 21):
        scores_on_1_hit.append(a)
        scores_on_1_hit.append(2*a)
        scores_on_1_hit.append(3*a)
    for a in range(1, 21):
        scores_double.append(2*a)

    for k in scores_double:
        if k < 100:
            compteur += 1
    for k in scores_on_1_hit:
        for u in scores_double:
            if k + u < 100:
                compteur += 1
    for i in range(len(scores_on_1_hit)):
        for j in range(i, len(scores_on_1_hit)):
            for u in scores_double:
                if scores_on_1_hit[i] + scores_on_1_hit[j] + u < 100:
                    compteur += 1

    print(compteur)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())