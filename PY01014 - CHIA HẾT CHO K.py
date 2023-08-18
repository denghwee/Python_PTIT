# I'm DengHwee or you can call me Chimmey

b = []
a, k, n = list(map(int, input().split()))
i = k - (a % k)
n -= a
while i <= n:
    b.append(i)
    i += k
if (len(b) == 0):
    print(-1)
else:
    for i in b:
        print(i, end = ' ')
