total_sum = 0
exit_1 = ''
while exit_1 != 'q':
    new_list_digit = []
    sum_numbers_list = 0
    print("Нажмите q, чтобы выйти")
    numbers_list = input("Введите число: ").split()
    for i in range(0, len(numbers_list)):
        if numbers_list[i].isdigit() == True:
            new_list_digit.append(int(numbers_list[i]))
        elif numbers_list[i] == 'q':
            exit_1 = 'q'
        else:
            print(f'{numbers_list[i]} - это не число! Вводите только числа')

    sum_numbers_list = sum(new_list_digit)
    total_sum += sum_numbers_list
    print(f'Сумма введёных чисел: {sum_numbers_list}, общая сумма: {total_sum}')
