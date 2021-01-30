from sys import argv
from itertools import cycle, count

sequence, number = argv
sequence_2 = argv


def sequence(number):
    num = 0
    try:
        number = int(number)
        for i in count(number):
            num += 1
            if num == 20:
                break
            else:
                print(i)
    except ValueError:
        print("Вы ввели букву, а надо вводить только цифры!")


sequence(number)


def sequence_2():
    count = 0
    list_1 = [1, 2, 3, 4]
    for i in cycle(list_1):
        count += 1
        if count == 20:
            break
        else:
            print(i)


sequence_2()
