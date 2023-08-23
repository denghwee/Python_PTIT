# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(a, b):
    if a < 2 or b < 2:
        return 'NO'
    sqr1 = int(sqrt(a)) + 1
    sqr2 = int(sqrt(b)) + 1
    for i in range(2, sqr1):
        if a % i == 0:
            return 'NO'
    for i in range(2, sqr2):
        if b % i == 0:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    s = input()
    print(check(int(s[0] + s[1] + s[2]), int(s[-3] + s[-2] + s[-1])))
