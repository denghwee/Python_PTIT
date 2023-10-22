# I'm DengHwee or you can call me Chimmey

a = []
for i in range(int(input())):
    s = input()
    if s not in a:
        a.append(s)
print(len(a))
