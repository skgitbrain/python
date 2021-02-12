class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        for i in self.list_1:
            for el in i:
                print(f"{el:3}", end="")
            print()
        return " "

    def __add__(self, other):
        for i in range(len(self.list_1)):
            for i_2 in range(len(other.list_1[i])):
                self.list_1[i][i_2] = self.list_1[i][i_2] + other.list_1[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2], [2, 3]])
m_2 = Matrix([[4, 5], [6, 7]])

print(m)
print(m + m_2)
