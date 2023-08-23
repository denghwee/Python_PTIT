# I'm DengHwee or you can call me Chimmey
from itertools import combinations

n, k = list(map(int, input().split()))
arr = list(set(map(int, input().split())))
arr.sort()
comb = list(combinations(arr, k))
for i in comb:
    for j in i:
        print(j, end = ' ')
    print()
