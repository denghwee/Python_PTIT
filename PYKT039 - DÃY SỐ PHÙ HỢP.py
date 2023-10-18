# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    check = 0
    for i in range(n):
        if a[i] > b[i]:
            check = 1
    if check == 1:
        print('NO')
    else:
        print('YES')
