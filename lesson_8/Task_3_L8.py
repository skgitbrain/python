class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


new_list = []
while True:
    number = input("введите число: ")
    try:
        if number == "stop":
            break

        elif number.isdigit() != True:
            raise MyError("Это не число! вводить нужно только числа")

        else:
            new_list.append(number)
    except MyError as err:
        print(err)
print(new_list)
