# I'm DengHwee or you can call me Chimmey

n = int(input())
a = list(map(int, input().split()))
num = 1
a.sort()
for i in a:
    if i == num:
        num += 1
    elif i > num:
        break
print(num)
