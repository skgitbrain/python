def my_func(num_1, num_2, num_3):
    list_1 = [num_1, num_2, num_3]
    list_1.remove(min(list_1))
    sum_1 = sum(list_1)
    return sum_1


print(my_func(1, 10, 3))
