class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        result = max(self.cell, other.cell) - min(self.cell, other.cell)
        if result > 0:
            return result
        else:
            return f'Разность клеток меньше 1, введите другие'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell)

    def make_order(self, rows):
        result = ''
        for i in range(int(self.cell / rows)):
            result += "*" * rows + '\n'
        result += '*' * (self.cell % rows) + '\n'
        return result


g = Cell(10)
g1 = Cell(2)
print(g + g1)
print(g - g1)
print(g * g1)
print(g / g1)
print(g.make_order(5))
