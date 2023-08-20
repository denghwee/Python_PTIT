# I'm DengHwee or you can call me Chimmey

num = []

def check(s):
    for i in s:
        if int(i) & 1 == 1:
            return False
    return True

def add(start, end):
    for i in range(start, end, 2):
        if check(str(i)) == True:
            num.append(i)

def sieve():
    add(10, 100)
    add(1000, 10000)
    add(100000, 1000000)

sieve()
for i in range(int(input())):
    n = int(input())
    for i in num:
        if i >= n:
            break
        if str(i) == str(i)[::-1]:
            print(i, end = ' ')
    print()
