import itertools

u = list(itertools.permutations(range(3)))[2][0:2]

for i in itertools.permutations(range(3)):
    print(i)

