# I'm DengHwee or you can call me Chimmey
from bisect import bisect_left

myMap = {}
a = []
for i in range(60):
    for j in range(38):
        for z in range(26):
            num = 2 ** i * 3 ** j * 5 ** z
            if num not in myMap:
                myMap[num] = 1
                a.append(num)
a.sort()

for i in range(int(input())):
    n = int(input())
    idx = bisect_left(a, n)
    if a[idx] != n:
        print('Not in sequence')
    else:
        print(idx+ 1)
