a = int(input("Введите результат спортсмена в первый день: "))
b = int(input("Введите цель по км, чтобы узнать на какой день она будет достигнута: "))

day = 1
while a < b:
    a += a * 0.1
    day += 1

print(f'на {day}-й день спортсмен достиг результата — не менее {b} км.')
