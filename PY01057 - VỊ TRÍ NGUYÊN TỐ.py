# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return False
    sqr = int(sqrt(n))
    for i in range(2, sqr + 1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    s = input()
    ans = 0
    for i in range(len(s)):
        if check(i) == True and check(int(s[i])) != True:
            ans = 1
        elif check(i) == False and check(int(s[i])) != False:
            ans = 1
    if ans == 0:
        print('YES')
    else:
        print('NO')
