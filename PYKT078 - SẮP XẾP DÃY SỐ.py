# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxNumber = max(a)
    for i in range(len(a)):
        if a[i] == maxNumber:
            a.insert(i, m)
            break
    b = []
    c = []
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)
    res = b + c
    for i in res:
        print(i, end = ' ')
    print()
