# I'm DengHwee or you can call me Chimmey

upper = 0
lower = 0
s = input()
for i in s:
    if i.isupper() == True:
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(s.upper())
else:
    print(s.lower())
