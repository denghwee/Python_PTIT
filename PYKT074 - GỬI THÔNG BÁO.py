# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    s = input()
    a = s.split()
    sum = 0
    for i in a:
        if sum != 0:
            sum += 1
        sum += len(i)
        if sum > 100:
            break
        print(i, end = ' ')
    print()
