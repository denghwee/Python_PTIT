# I'm DengHwee or you can call me Chimmey

def solve():
    s = input()
    if s[len(s)-1] == '6' and s[len(s)-2] == '8':
        print('YES')
    else:
        print('NO')

t = int(input())
while t > 0:
    t -= 1
    solve()
