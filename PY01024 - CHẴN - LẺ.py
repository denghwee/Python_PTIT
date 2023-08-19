# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    check = 0
    totalSum = int(s[0])
    for i in range(1, len(s)):
        totalSum += int(s[i])
        if abs(int(s[i-1]) - int(s[i])) != 2:
            check = 1
    if totalSum % 10 != 0:
        check = 1
    if check == 1:
        print('NO')
    else:
        print('YES')
