# I'm DengHwee or you can call me Chimmey

def check(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

t = int(input())
a = []
num = 2
while num <= 888:
    if check(str(num)):
        tmp = str(num)
        a.append(int(tmp + tmp[::-1]))
    num += 2
while t > 0:
    t -= 1
    n = int(input())
    for i in a:
        if i >= n:
            break
        else:
            print(i, end = ' ')
    print()
