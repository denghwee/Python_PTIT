# I'm DengHwee or you can call me Chimmey

n = int(input())
ans = 0
a = list(map(int, input().split()))
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            ans += 1
print(ans)
