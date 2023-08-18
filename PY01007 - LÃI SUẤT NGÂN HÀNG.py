# I'm DengHwee or you can call me Chimmey

test = int(input())
for i in range(test):
    cnt = 0
    n, x, m = list(map(float, input().split()))
    while n < m:
        tmp = n * (x / 100)
        n += tmp
        cnt += 1
    print(cnt)
