# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    check = 0
    a = input().split('.')
    if len(a) == 4:
        for i in a:
            if i.isdigit():
                if int(i) < 0 or int(i) > 255:
                    check = 1
                    break
            else:
                check = 1
                break
        if check == 1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
