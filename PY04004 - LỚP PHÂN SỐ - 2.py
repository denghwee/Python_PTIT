# I'm DengHwee or you can call me Chimmey
import math

class fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compact(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def __add__(self, other):
        self.sumA = self.a * other.b + other.a * self.b
        self.sumB = self.b * other.b
        res = fraction(self.sumA, self.sumB)
        res.compact()
        return res
    
x1, y1, x2, y2 = map(int, input().split())
fraction1 = fraction(x1, y1)
fraction2 = fraction(x2, y2)
ans = fraction1 + fraction2
print(f"{ans.a}/{ans.b}")
