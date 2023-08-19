# I'm DengHwee or you can call me Chimmey

def solve():
    s = input()
    ans = ''
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            ans += str(cnt) + s[i - 1]
            cnt = 1
        else:
            cnt += 1
    ans += str(cnt) + s[len(s) - 1]
    print(ans)

t = int(input())
while t > 0:
    t -= 1
    solve()
