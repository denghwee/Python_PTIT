# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    check = 0
    if s[0] == s[1]:
        print('NO')
    for i in range(2, len(s)):
        if s[i] != s[i & 1]:
            check = 1
            break
    if check == 0:
        print('YES')
    else:
        print('NO')
