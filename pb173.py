import time


start = time.perf_counter()
total = 0
for i in range(1, 250002):
    for j in range(i+2, 250002, 2):
        if (j+i) * (j-i) <= 1000000:
            total += 1
        else:
            break
print(total)
print('temps d execution', time.perf_counter() - start, 'sec')
