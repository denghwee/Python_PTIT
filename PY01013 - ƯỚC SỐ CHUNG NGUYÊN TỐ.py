# I'm DengHwee or you can call me Chimmey
import math

def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(math.sqrt(n)) + 1
    for i in range(5, sqr, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def sumDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

t = int(input())
while t > 0:
    t -= 1
    List = list(map(int, input().split()))
    a, b = List
    if isPrime(sumDigit(math.gcd(a, b))):
        print("YES")
    else:
        print("NO")
