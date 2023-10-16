# I'm DengHwee or you can call me Chimmey
for i in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    tmp1 = a + c
    tmp2 = b + d
    res1 = [tmp1 * a - tmp2 * b, tmp1 * b + tmp2 * a]
    res2 = [tmp1 * tmp1 - tmp2 * tmp2, tmp1 * tmp2 + tmp1 * tmp2]
    print(res1[0], end = ' ')
    if res1[1] < 0:
        print('-', end = ' ')
    else:
        print('+', end = ' ')
    print(f'{abs(res1[1])}i, ', end = '')
    print(res2[0], end = ' ')
    if res2[1] < 0:
        print('-', end = ' ')
    else:
        print('+', end = ' ')
    print(f'{abs(res2[1])}i')
