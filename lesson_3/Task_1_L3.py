num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
if num_2 == 0:
    while num_2 == 0:
        print("На ноль делить нельзя, введите другое число")
        num_2 = float(input("Введите второе число: "))


def numbers(num_1, num_2):
    result = num_1 / num_2
    return result


print(numbers(num_1, num_2))
