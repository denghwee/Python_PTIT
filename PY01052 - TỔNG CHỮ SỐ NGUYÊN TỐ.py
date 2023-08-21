# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return 'NO'
    sqr = int(sqrt(n))
    for i in range(2, sqr + 1):
        if n % i == 0:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    print(check(sum))
