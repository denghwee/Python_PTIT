# I'm DengHwee or you can call me Chimmey

a = [1]
for i in range(1, 10):
    res = 1
    for j in range(1, i + 1):
        res *= j
    a.append(res)
for i in range(int(input())):
    s = input()
    res = 0
    for i in range(len(s)):
        res += a[int(s[i])]
    if res == int(s):
        print('Yes')
    else:
        print('No')
