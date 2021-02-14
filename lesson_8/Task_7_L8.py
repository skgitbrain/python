class Complex:
    def __init__(self, num_1=0, num_2=0):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f'{self.num_1}'

    def __add__(self, other):
        result = (self.num_1 + other.num_1) + (self.num_2 + other.num_2)
        return Complex(result)

    def __mul__(self, other):
        result = (self.num_1 * other.num_1 + self.num_1 * other.num_2) \
                 + self.num_2 * other.num_1 + self.num_2 * other.num_2
        return Complex(result)


g = Complex(1, 2j)
g1 = Complex(2, 3j)
print(g + g1)
print(g * g1)
