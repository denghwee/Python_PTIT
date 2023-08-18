# I'm DengHwee or you can call me Chimmey

t = int(input())
while t > 0:
    t -= 1
    s = input()
    if s[0] == s[-2] and s[1] == s[-1]:
        print('YES')
    else:
        print('NO')
