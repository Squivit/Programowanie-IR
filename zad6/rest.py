class Element:
    def __init__(self, res=0) -> None:
        self.value = int(res) % 17
    def __add__(self, other):
        return Element((self.value + other.value)%17)
    def __iadd__(self,other):
        return Element((self.value + other.value)%17)
    def __mul__(self,other):
        return Element((self.value * other.value)%17)
    def __imul__(self,other):
        return Element((self.value * other.value)%17)
    def __str__(self) -> str:
        return self.value

import sys

arg = sys.argv[1:3]

e1 = Element(arg[0])
e2 = Element(arg[1])

print(e1 + e2)
print(e1 * e2)
