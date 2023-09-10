import math
class rational:
    def __init__(self,x,y):
        self.num = x
        self.denom = y
    def __str__(self):
        return str(self.num) + '\n' + '-' + '\n' + str(self.denom)
    def redc(self):
        k = math.gcd(self.num, self.denom)
        self.num= self.num // k
        self.denom= self.denom // k
    def __mul__(self,rational_2):
        a = self.num * rational_2.num
        b = self.denom * rational_2.denom
        c = rational(a,b)
        c.redc()
        return c
    def __truediv__(self,rational_2: int):
        self.num *= rational_2.denom
        self.denom *= rational_2.num
    def __add__(self,rational_2: int):
        a = self.num * rational_2.denom + self.denom * rational_2.num
        b = self.denom * rational_2.denom
        c = rational(a,b)
        c.redc()
        return c
    def __sub__(self,rational_2: int):
        a = self.num * rational_2.denom - self.denom * rational_2.num
        b = self.denom * rational_2.denom
        c = rational(a, b)
        c.redc()
        return c








rational_1 = rational(15,75)
rational_2 = rational(1,5)
rational_3 = rational_1 * rational_2
rational_4 = rational_1 + rational_2
rational_5 = rational_1 - rational_2
print(rational_5)



