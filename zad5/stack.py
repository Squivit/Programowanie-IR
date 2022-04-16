class Stack:
    def __init__(self, *args) -> None:
        self.list = list(args)
    def return_inverse(self) -> float:
        a = len(self.list) -1
        art = []
        for i in range(a + 1):
            art.append(self.list[a-i])
        return art


s = Stack(4, 6, 2, 7, 3, 5, 6)
print(s.return_inverse())