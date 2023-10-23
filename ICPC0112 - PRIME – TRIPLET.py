# I'm DengHwee or you can call me Chimmey

a = [0] * 1000001

def erastosthenes():
    a[0] = a[1] = 1
    for i in range(2, 1001):
        if a[i] == 0:
            for i in range(i * i, 1000001, i):
                a[i] = 1

erastosthenes()
for i in range(int(input())):
    res = 0
    n = int(input())
    for i in range(n - 6):
        if a[i] == a[i+2] == a[i+6] == 0:
            res += 1
        if a[i] == a[i+4] == a[i+6] == 0:
            res += 1
    print(res)
