# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s1 = input()
    s2 = ''
    check = 0
    for i in range(1000):
        if int(s1) % 7 == 0:
            check = 1
            break
        s2 = s1[::-1]
        s1 = str(int(s1) + int(s2))
    if check == 0:
        print(-1)
    else:
        print(s1)
