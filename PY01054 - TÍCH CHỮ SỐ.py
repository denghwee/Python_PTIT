# I'm DengHwee or you can call me Chimmey
from math import sqrt

for i in range(int(input())):
    s = input()
    product = 1
    for i in s:
        if i != '0':
            product *= int(i)
    print(product)
