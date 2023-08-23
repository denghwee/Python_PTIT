# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return 'NO'
    sqr = int(sqrt(n)) + 1
    for i in range(2, sqr):
        if n % i == 0:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    s = input()
    print(check(int(s[-4] + s[-3] + s[-2] + s[-1])))
