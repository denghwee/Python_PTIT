# I'm DengHwee or you can call me Chimmey

while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
        break
    ans = 0
    while True:
        if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
            break
        a0 = abs(a[0] - a[1])
        a1 = abs(a[1] - a[2])
        a2 = abs(a[2] - a[3])
        a3 = abs(a[3] - a[0])
        a[0] = a0
        a[1] = a1
        a[2] = a2
        a[3] = a3
        ans += 1
    print(ans)
