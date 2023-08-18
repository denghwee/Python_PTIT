# I'm DengHwee or you can call me Chimmey

t = int(input())
while t > 0:
    t -= 1
    s = input()
    check = 0
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            check = 1
            break
    if check == 0:
        print('YES')
    else:
        print('NO')
