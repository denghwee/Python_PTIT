# I'm DengHwee or you can call me Chimmey

a = []
for i in range(int(input())):
    a.append(input())
cnt = 0
check = 0
res1 = 0
res2 = []
for i in a:
    if len(i.split()) == 7:
        if check == 1:
            check = 0
            res1 += 1
            res2.append(1)
        cnt += 1
        if cnt == 4:
            res1 += 1
            cnt = 0
            res2.append(2)
    else:
        check = 1
if check == 1:
    check = 0
    res1 += 1
    res2.append(1)
print(res1)
for i in res2:
    print(i)
