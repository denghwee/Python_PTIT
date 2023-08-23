# I'm DengHwee or you can call me Chimmey

ans = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        ans += 1
print(ans)
