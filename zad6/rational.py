class Rational:
    def __init__(self, p=0, q=1) -> None:
        self.error = False
        if type(p) == str and p.__contains__('/'):
            p, q = p.split('/')
        p = int(p)
        q = int(q)
        if q == 0:
            print('Nie można dzielić przez 0')
            self.error= True
        else:
            from math import gcd
            a = gcd(p,q)
            if a != 1:
                p = int(p/a)
                q = int(q/a)
            if q < 0:
                p = -p
                q = -q
            self.p = p
            self.q = q
    def numerator(self):
        return self.p
    def denominator(self):
        return self.q
    def float(self):
        if not self.error:
            return self.p/self.q
    def __neg__(self):
        return Rational(-self.p, self.q)
    def __str__(self) -> str:
        if self.error:
            return 'Liczba nie istnieje'
        elif self.p == 0:
            return str(0)
        elif self.q == 1:
            return str(self.p)
        else:
            return str(self.p) + '/' + str(self.q)



r = Rational(128, -48)
l = Rational(-0, 3)
h = Rational(-6, 3)
i = Rational(-2, 0)

print(r, l, h, i)