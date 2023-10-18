# I'm DengHwee or you can call me Chimmey

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    res = ''
    n, k = list(map(int, input().split()))
    while n > 0:
        tmp = n % k
        res = alphabet[tmp] + res
        n = int(n / k)
    print(res)
