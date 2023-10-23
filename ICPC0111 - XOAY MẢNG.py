# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(d, n):
        print(a[i], end = ' ')
    for i in range(d):
        print(a[i], end = ' ')
    print()
