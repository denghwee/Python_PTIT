# I'm DengHwee or you can call me Chimmey
from math import gcd

imp = list(map(int, input().split()))
n, k = imp
start = 10 ** (k - 1)
end = 10 ** k
cnt = 0
for i in range(start, end - 1):
    if gcd(n, i) == 1:
        print(i, end = ' ')
        cnt += 1
    if cnt == 10:
        cnt = 0
        print()
