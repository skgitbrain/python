revenue = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if costs > revenue:
    print("Фирма терпит убытки")
elif costs == revenue:
    print("Фирма вышла в ноль")
else:
    print("Фирма вышла на прибыль")
    profit = revenue - costs
    profitability = profit / revenue
    print("Рентабельность:", profitability)
    num_of_employees = int(input("Введите кол-во сотрудников: "))
    profit_per_employee = profit / num_of_employees
    print("Прибыль фирмы в расчёте на одного сотрудника:", profit_per_employee)
