# I'm DengHwee or you can call me Chimmey
import sys
import array
import math

N, M = 1 + 2*10**6,2*10**6
c = array.array('i', [0]*N)
for i in range(2,int(math.sqrt(M))+1):
	if c[i]==0:
		c[i] = i
		for j in range(i,M//i+1):
			c[i*j] = i
del j
del M
for i in range(4,N):
	c[i] += c[i//c[i]] if c[i] else i
del N
del i
ans = 0
n = int(sys.stdin.readline())
while True:
    try:
        x = int(sys.stdin.readline())
        ans += c[x]
    except: break
print(ans)
