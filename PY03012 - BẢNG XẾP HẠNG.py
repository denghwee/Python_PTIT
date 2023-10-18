# I'm DengHwee or you can call me Chimmey
import functools

class Student:
    def __init__(self, name, accepted, submitted):
        self.name = name
        self.accepted = accepted
        self.submitted = submitted

def cmp(a, b):
    if a.accepted < b.accepted:
        return 1
    elif a.accepted == b.accepted:
        if a.submitted > b.submitted:
            return 1
        elif a.submitted == b.submitted:
            if a.name > b.name:
                return 1
    return -1

a = []
for i in range(int(input())):
    name = input()
    accepted, submitted = list(map(int, input().split()))
    a.append(Student(name, accepted, submitted))
a = sorted(a, key = functools.cmp_to_key(cmp))
for i in a:
    print(i.name, i.accepted, i.submitted)
