# I'm DengHwee or you can call me Chimmey
from itertools import permutations

s = input()
perm = list(permutations(s))
for i in perm:
    for j in i:
        print(j, end = '')
    print()
