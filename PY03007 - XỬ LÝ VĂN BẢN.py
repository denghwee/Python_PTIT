# I'm DengHwee or you can call me Chimmey
import re

s = ''
regex = '[\w\s,:]+'
while True:
    try : s += input()
    except EOFError: break
res = re.findall(regex, s)
for i in res:
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))
