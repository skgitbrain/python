list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list =[]
for i in range(len(list_1)):
    count = 0
    for x in list_1:
        if x == list_1[i]:
            count +=1
    if count == 1:
        new_list.append(list_1[i])


print(new_list)