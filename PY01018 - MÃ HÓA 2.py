# I'm DengHwee or you can call me Chimmey

P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

def solve():
    while True:
        inp = input()
        if inp[0] == '0':
            break
        k, s = inp.split()
        res = ''
        for i in s:
            res += P[(P.find(i) + int(k)) % 28]
        print(res[::-1])

solve()
