class SortedList:
    def __init__(self, list):
        self.list = list
        self.list.sort()
    def append(self, element):
        self.list.extend(element)
        self.list.sort()
    def __str__(self):
        return f'{[x for x in self.list]}'

sl = SortedList([2,7,3,8,1,65,12])
print(sl)
sl.append([426, 8239, 3, 0, -5748, -9])
print(sl)