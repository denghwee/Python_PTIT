# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return False
    sqr = int(sqrt(n) + 1)
    for i in range(2, sqr):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
myMap = {}
for i in a:
    if i not in myMap:
        if check(i) == True:
            myMap[i] = 1
    else:
        myMap[i] += 1
for f, s in myMap.items():
    print(f, s)
