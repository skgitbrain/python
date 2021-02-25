class Warehouse:

    @staticmethod
    def add_warehouse():
        list_1 = []
        stop = "stop"
        while True:
            print("Чтобы выйти, напишите 'stop'")
            name = input("Введите название техники: ")
            if name == stop:
                break

            quantity = ''
            while quantity.isdigit() == False:

                try:
                    quantity = input("Введите кол-во: ")
                    if quantity == stop:
                        return list_1
                    int(quantity)

                except ValueError:
                    if quantity == stop:
                        break
                    print('Вводить нужно только число!')

            division = input("В какое подразделение передать технику: ")
            if division == stop:
                break

            list_1.append({"name": name, "quantity": quantity, "division": division})

        return list_1


class Office_equipment:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'Техника: {self.name}, количество {self.quantity}, цена {self.price}'


class Printer(Office_equipment):

    def __init__(self, name, quantity, price, printer_type):
        super().__init__(name, quantity, price)
        self.printer_type = printer_type

    def __str__(self):
        return f'Техника: {self.name}, количество {self.quantity}, цена {self.price}, тип принтер {self.printer_type}'


class Scaner(Office_equipment):
    def __init__(self, name, quantity, price, scaner_type):
        super().__init__(name, quantity, price)
        self.scaner_type = scaner_type

    def __str__(self):
        return f'Техника: {self.name}, количество {self.quantity}, цена {self.price}, тип Сканера {self.scaner_type}'


class Xerox(Office_equipment):
    def __init__(self, name, quantity, price, xerox_type):
        super().__init__(name, quantity, price)
        self.xerox_type = xerox_type

    def __str__(self):
        return f'Техника: {self.name}, количество {self.quantity}, цена {self.price}, тип Ксерокса {self.xerox_type}'


print(Warehouse.add_warehouse())
g = Xerox("Принтер", 2, 100, "Струйный")
print(g)
