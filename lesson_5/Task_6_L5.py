new_dic = {}


def digit_1(num):
    char = ""
    for i in num:
        if i.isdigit():
            char += i
    if char == "":
        return 0
    else:
        return int(char)


with open("txttask_6.txt", "r", encoding="utf-8") as f:
    for i in f:
        new_dic[i.split()[0][0:-1]] = digit_1(i.split()[1]) + digit_1(i.split()[2]) + digit_1(i.split()[3])
print(new_dic)
