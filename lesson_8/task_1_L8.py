class Data:
    def __init__(self, text):
        self.text = text

    @classmethod
    def method_1(cls, text):
        data_1 = text.split("-")
        return int(data_1[0]), int(data_1[1]), int(data_1[2])

    @staticmethod
    def method_2(text):
        data_1 = text.split("-")
        if 0 <= int(data_1[0]) <= 31 and 1 <= int(data_1[1]) <= 12 and 1930 <= int(data_1[2]) <= 2999:
            return text
        else:
            return f"Вы указали неверную дату"


print(Data.method_1('01-02-2021'))
print(Data.method_2('01-02-2209'))
