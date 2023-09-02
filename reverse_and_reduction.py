import math
class reduction:
    def __init__(self,x,y):
        self.num= x
        self.denom = y
    def print(self):
        print(self.num)
        print('-')
        print(self.denom)
    def redc(self):
        global k
        k = math.gcd(self.num, self.denom)
        print(k)
    def devide(self):
        n = self.num // k
        d = self.denom // k
        print(n)
        print("-")
        print(d)


reduction_1 = reduction(15,75)
reduction_1.print()
reduction_1.redc()
reduction_1.devide()

