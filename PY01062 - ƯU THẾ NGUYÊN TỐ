# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    s = input()
    primeNum = 0
    if check(len(s)) == False:
        print('NO')
        continue
    for i in s:
        if check(int(i)) == True:
            primeNum += 1
    if primeNum <= len(s) - primeNum:
        print('NO')
    else:
        print('YES')
