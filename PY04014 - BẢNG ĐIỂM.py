# I'm DengHwee or you can call me Chimmey
from decimal import ROUND_HALF_UP, Decimal

a = {}
for j in range(int(input())):
    name = input()
    scores = [Decimal(x) for x in input().split()]
    mean = (scores[0] + scores[1]) * 2
    for i in range(2, 10):
        mean += scores[i]
    mean /= 12
    mean = mean.quantize(Decimal('0.1'), ROUND_HALF_UP)
    a[name] = (j + 1, mean)
a = dict(sorted(a.items(), key = lambda item : item[1][1], reverse = True))
for i in a:
    print('HS{:02d}'.format(a[i][0]), i, a[i][1], end = ' ')
    if a[i][1] < 5 : print('YEU')
    elif a[i][1] < 7 : print('TB')
    elif a[i][1] < 8 : print('KHA')
    elif a[i][1] < 9 : print('GIOI')
    else : print('XUAT SAC')
