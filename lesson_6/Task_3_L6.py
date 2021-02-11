class Worker:
    def __init__(self, name, suname, position, wage, bonus):
        self.name = name
        self.suname = suname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, suname, position, wage, bonus):
        super().__init__(name, suname, position, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.suname}")

    def get_total_income(self):
        print(f"Доход с учётом премии: {self._income['wage'] + self._income['bonus']}")


r = Position("Игорь", "Соловьёв", "Программист", 100000, 30000)
r.get_full_name()
r.get_total_income()
