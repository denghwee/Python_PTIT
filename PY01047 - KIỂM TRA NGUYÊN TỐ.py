# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return 'NO'
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    s = input()
    num = s[-4] + s[-3] + s[-2] + s[-1]
    print(check(int(num))) 
