# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    res = 0
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        x = a[i]
        while l < r:
            if x + a[l] + a[r] == 0:
                res += 1
                l += 1
            elif x + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    print(res)
