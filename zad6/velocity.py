class Velocity:
    def __init__(self, beta = 0) -> None:
        self.beta = beta

    def gamma(self):
        import math as m
        return 1 / m.sqrt(1 - self.beta**2)

    def __add__(self, other):
        return ( self.beta + other.beta ) / (1+self.beta*other.beta)
    
    def __iadd__(self, other):
        self.beta = ( self.beta + other.beta ) / (1+self.beta*other.beta)
        return self



v1 = Velocity(.2)
v2 = Velocity(.5)

print(v1 + v2)
v1 += v2

print(v1.beta)