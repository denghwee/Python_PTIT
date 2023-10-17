# I'm DengHwee or you can call me Chimmey

a = {}
for i in range(int(input())):
    name = input()
    point_1 = float(input())
    point_2 = float(input())
    if point_1 > 10:
        point_1 /= 10
    if point_2 > 10:
        point_2 /= 10
    point = (point_1 + point_2) / 2
    a[name] = (i + 1, point)
a = dict(sorted(a.items(), key = lambda item : item[1][1], reverse = True))
for i in a:
    print('TS0{:d}'.format(a[i][0]), i, '{:.2f}'.format(a[i][1]), end = ' ')
    if a[i][1] < 5:
        print('TRUOT')
    elif a[i][1] < 8:
        print('CAN NHAC')
    elif a[i][1] < 9.5:
        print('DAT')
    else:
        print('XUAT SAC')
