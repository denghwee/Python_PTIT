# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check1(n):
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
    check = 0
    for i in range(len(s)):
        sum += int(s[i])
        if i & 1 == 1 and int(s[i]) & 1 != 1:
            print('NO')
            check = 1
            break
        if i & 1 == 0 and int(s[i]) & 1 != 0:
            print('NO')
            check = 1
            break
    if check == 0:
        print(check1(sum))
