# I'm DengHwee or you can call me Chimmey

t = int(input())
while t > 0:
    t -= 1
    s = input()
    ans = ''
    tmp = ''
    for i in s:
        if i.isalpha() == True:
            tmp = i
        else:
            loop = int(i)
            while loop > 0:
                loop -= 1
                ans += tmp
    print(ans)
