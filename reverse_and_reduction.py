
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


