my_list = [7, 5, 3, 3, 2, 0]
while True:
    number = input("Введите число или напишите exit, чтобы выйти: ")
    if number == "exit":
        break
    else:
        number = int(number)
        max_length = len(my_list)

        for y in range(0, max_length):
            if number >= my_list[y]:
                num = y
                break

        my_list = my_list[0:num] + [number] + my_list[num:max_length + 1]
        print(my_list)
