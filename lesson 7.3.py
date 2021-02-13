import colorama
from colorama import Fore, Back, Style
class Cell:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Fore.BLUE + f"Увеличение клетки. Теперь ее размер: {self.a + other.a}"
    def __sub__(self, other):
        return Fore.BLUE + f"Уменьшение клетки. Теперь ее размер: {self.a - other.a}"
    def __mul__(self, other):
        return Fore.BLUE + f"Клетка увеличилась в несколько раз. Теперь ее размер: {self.a * other.a}"
    def __truediv__(self, other):
        return Fore.BLUE + f"Клетка уменьшилась в несколько раз. Теперь ее размер: {self.a / other.a}"
    def make_order(self, rows):
        return Fore.GREEN + '\n'.join(["*" * rows for _ in range(self.a // rows)]) + '\n' + "*" * (self.a % rows)


cell1 = Cell(int(input("Первая клетка: ")))
cell2 = Cell(int(input("Вторая клетка: ")))
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
print(cell1.make_order(5))



