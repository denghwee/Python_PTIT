# I'm DengHwee or you can call me Chimmey

s = input()
s = s[::-1]
ans = ''
cnt = 0
for i in s:
    if cnt == 3:
        cnt = 0
        ans += ','
    cnt += 1
    ans += i
print(ans[::-1])
