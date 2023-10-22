# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    res = 0
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, len(a)):
        if abs(a[i-1] - a[i]) > 1:
            res += (abs(a[i-1] - a[i]) - 1)
    print(res)
