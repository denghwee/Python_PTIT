# I'm DengHwee or you can call me Chimmey

a = []
res = 0
n = int(input())
for i in range(n):
    a.append(input())
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][j] == 'C':
            cnt += 1
    res += int((cnt * (cnt - 1)) / 2)
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j][i] == 'C':
            cnt += 1
    res += int((cnt * (cnt - 1)) / 2)
print(res)
