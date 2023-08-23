# I'm DengHwee or you can call me Chimmey
from math import gcd

def reduceBigNum(a, b):
    mod = 0
    for i in range(len(b)):
        mod = (mod * 10 + int(b[i])) % a
    return mod

def findGCD(a, b):
    b = reduceBigNum(a, b)
    return gcd(a, b)

for i in range(int(input())):
    a = int(input())
    b = input()
    print(findGCD(a, b))
