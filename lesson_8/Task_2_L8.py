class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = int(input("На сколько частей будет делить апельсин?: "))
try:
    if num_1 == 0:
        raise MyError("На ноль делить нельзя!")
except MyError as err:
    print(err)

else:
    print(f'Получится вот столько целых долек {int(6 / num_1)}')
