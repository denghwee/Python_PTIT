# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum < 10:
        print('NO')
    elif str(sum) == str(sum)[::-1]:
        print('YES')
    else:
        print('NO')
