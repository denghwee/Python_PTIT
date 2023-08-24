# I'm DengHwee or you can call me Chimmey

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    a = set()
    a.add(n)
    while True:
        if n & 1 == 0:
            n //= 2
            a.add(n)
        else:
            n = n * 3 + 1
            a.add(n)
        if n == 1:
            break
    print(len(a))
