# I'm DengHwee or you can call me Chimmey
from math import gcd

F = []
F.append(0)
def fibonacci():
    F.append(1)
    F.append(1)
    for i in range(3, 93):
        F.append(F[len(F) - 2] + F[-1])

fibonacci()
for i in range(int(input())):
    a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        print(F[i], end = ' ')
    print()
