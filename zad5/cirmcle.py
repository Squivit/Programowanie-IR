from cmath import inf


class Circle:
    import math as m
    def __init__(self, x=0, y=0, r=1):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
    def circumference(self):
        return 2 * self.m.pi * self.r
    def intersection(self, other_circle):
        dis = self.m.sqrt((self.x - other_circle.x)**2 + (self.y - other_circle.y)**2)
        sum = self.r + other_circle.r
        diff = abs(self.r - other_circle.r)
        concentric = False
        if dis < self.r and dis < other_circle.r:
            concentric = True
        if diff == 0 and concentric:
            return inf
        if concentric:
            if dis == diff:
                return 1
            elif dis < diff:
                return 0
            elif dis > diff:
                return 2
        else:
            if dis == sum:
                return 1
            elif diff < dis < sum:
                return 2
            else:
                return 0


import sys
import math
argv = sys.argv[1:]
circ1 = Circle(*argv[:3])
circ2 = Circle(*argv[3:])

sect = circ1.intersection(circ2)
if math.isinf(sect):
    print('Okręgi są współśrodkowe!')
else:
    print(f'Ilość punktów wspólnych: {sect}')