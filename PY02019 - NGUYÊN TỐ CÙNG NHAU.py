# I'm DengHwee or you can call me Chimmey
from math import gcd

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], end = ' ')
            print(a[j])
