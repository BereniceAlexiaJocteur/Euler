import itertools


for i in itertools.combinations_with_replacement(range(1, 13), 20):
    print(i)