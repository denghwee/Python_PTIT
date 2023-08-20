# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    check = 0
    for i in s:
        if i != '0' and i != '1' and i != '2':
            check = 1
            break
    if check == 0:
        print('YES')
    else:
        print('NO')
