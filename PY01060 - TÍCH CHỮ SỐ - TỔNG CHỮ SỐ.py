# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    sum = 0
    product = 1
    check = 0
    for i in range(len(s)):
        if i & 1 == 0:
            if int(s[i]) != 0:
                check = 1
                product *= int(s[i])
        else:
            sum += int(s[i])
    if check == 0:
        product = 0
    print(product, end = ' ')
    print(sum)
