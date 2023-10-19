# I'm DengHwee or you can call me Chimmey

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    b = int(input())
    a = int(input(), 2) 
    res = ''
    while a > 0:
        tmp = a % b
        res = alphabet[tmp] + res
        a = int(a / b)
    print(res)
