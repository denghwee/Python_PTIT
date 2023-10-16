# I'm DengHwee or you can call me Chimmey

def time(x, y):
    return y[0] * 60 + y[1] - x[0] * 60 - x[1]

a = {}
for i in range(int(input())):
    name = input()
    x = [int(i) for i in input().split(':')]
    y = [int(i) for i in input().split(':')]
    values = int(input())
    if name not in a:
        a[name] = (time(x, y), values)
    else:
        a[name] = (a[name][0] + time(x, y), a[name][1] + values)
num = 1
for i in a:
    print('T{:02d}'.format(num), i, '{:.2f}'.format(a[i][1] * 60 / a[i][0]))
    num += 1
