from random import random

class Person:
    maxDistance = 1
    maxIllDistance = .1
    w = 100
    h = 100
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.stat = 0
    def status(self):
        if self.stat == 0:
            return 'zdrowy'
        if self.stat == 1:
            return 'nosiciel'
        else:
            return 'chory'
    def move(self):
        import math
        if self.stat == 2:
            d = self.maxIllDistance
        else:
            d = self.maxDistance
        d *= random()
        fi = random() * 2 * math.pi
        self.x += d * math.cos(fi)
        self.y += d * math.sin(fi)
        if self.x > self.w:
            self.x -= self.w
        if self.x < 0:
            self.x += self.w
        if self.y > self.h:
            self.y -= self.h
        if self.y < 0:
            self.y += self.h
    def info(self):
        return f'Położenie: ({self.x}, {self.y}), status osoby: {self.status()}'
    def __str__(self) -> str:
        return self.info()

class Population:
    people = []
    w = 0
    h = 0
    infectionProbability = .2
    infectionDistance = 1
    def __init__(self, w=100, h=100, pop=20) -> None:
        pass

p = Person(3, 2)
print(p)
for i in range(10):
    p.move()
    print(p)