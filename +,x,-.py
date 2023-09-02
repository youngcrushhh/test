class plus:
    def __init__(self,x,y):
        self.addendum_1= x
        self.addendum_2 = y
    def sum(self):
        s = self.addendum_1 + self.addendum_2
        print(s)


plus_1 = plus(1,7)
plus_1.sum()

print("--------------------------")


class times:
    def __init__(self, x, y):
        self.multiplier_1 = x
        self.multiplier_2 = y

