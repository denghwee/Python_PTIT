# I'm DengHwee or you can call me Chimmey
from math import sqrt

def check(s):
    if len(s) & 1 == 0 or s[0] == s[1]:
        return 'NO'
    for i in range(2, len(s), 2):
        if s[i-2] != s[i]:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    s = input()
    print(check(s))
