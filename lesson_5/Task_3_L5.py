new_list = []
with open('txttask_3.txt', "r", encoding='utf-8') as f:
    print(f"Сотрудники, которые имеют оклад менее 20 тыс:")
    for i in f:
        new_list.append(float(i.split()[1]))
        if float(i.split()[1]) < 20000:
            print(i.split()[0] + " " + i.split()[1])

print(f'Средняя зарплата сотрудника: {sum(new_list) / len(new_list)}')
