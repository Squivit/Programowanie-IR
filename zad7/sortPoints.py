from venv import create


class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        self.update_len()
    def update_len(self):
        from math import sqrt
        self.__len = sqrt(self.__x**2 + self.__y**2)
    @property
    def X(self):
        return self.__x
    @X.setter
    def X(self, val):
        self.__x = val
        self.update_len()
    @property
    def Y(self):
        return self.__y
    @Y.setter
    def Y(self, val):
        self.__y = val
        self.update_len()
    @property
    def len(self):
        return self.__len


def sortPoints(points, sort_method):
    met1 = lambda p: p.X
    met2 = lambda p: p.Y
    met3 = lambda p: p.len
    met = [met1, met2, met3]
    for p in points:
        print(f'({p.X}, {p.Y}), len = {p.len}')
    print('______')
    print('Sortowane po x:')
    for p in sorted(points, key=met[0]):
        print(f'({p.X}, {p.Y})')
    print('______')
    print('Sortowane po y:')
    for p in sorted(points, key=met[1]):
        print(f'({p.X}, {p.Y})')
    print('______')
    print('Sortowane po dlug:')
    for p in sorted(points, key=met[2]):
        print(f'({p.X}, {p.Y}), len = {p.len}')


import sys

argv = sys.argv[1:]
str.split(',')

sortPoints([Point(int(x.split(',')[0]), int(x.split(',')[1])) for x in argv[1:]], int(argv[0]))