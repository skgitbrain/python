list_1 = []
exit_input = ":q!"
while True:
    entering_indexes = input("Введите элемент для списка: ")
    if entering_indexes == exit_input:
        break
    list_1.append(entering_indexes)
    print(f'Введите "{exit_input}", если вы хотите выйти из режима ввода элементов')
if len(list_1) == 1:
    print(list_1)

else:
    for i in range(0, len(list_1) - 1, 2):
        list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
    print(list_1)
