# I'm DengHwee or you can call me Chimmey

a = {}
for j in range(int(input())):
    name = input()
    old = int(input())
    new = int(input())
    s = new - old
    if s > 100:
        s = 50 * 100 + 50 * 150 + (s - 100) * 200
        s += s * 0.05
    elif s > 50:
        s = 50 * 100 + (s - 50) * 150
        s += s * 0.03
    else:
        s *= 100
        s += s * 0.02
    s = round(s)
    a[name] = (j + 1, s)
a = dict(sorted(a.items(), key = lambda item : item[1][1], reverse = True))
for i in a:
    print('KH{:02d}'.format(a[i][0]), i, a[i][1])
