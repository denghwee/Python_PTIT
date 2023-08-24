# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    myMap = {}
    num = int(1e7)
    for i in a:
        if i not in myMap:
            myMap[i] = 1
        else:
            myMap[i] += 1
    fmax = max(myMap.values())
    for f, s in myMap.items():
        if s == fmax:
            num = min(f, num)
    if fmax > n / 2:
        print(num)
    else:
        print('NO')
