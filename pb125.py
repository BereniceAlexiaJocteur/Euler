import time


start = time.perf_counter()
limit = 10000
sum = 0
liste = []


def palindrome(s):
    return s == s[::-1]


for i in range(1, limit+1):
    number = i*i
    for j in range(i+1, limit+1):
        number += j*j
        if number > 100000000:
            break
        if palindrome(str(number)) and not(number in liste):
            sum += number
            liste.append(number)
print(sum)
print('temps d\'exécution', time.perf_counter() - start, 'sec')