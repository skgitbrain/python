alphabet = set("qwertyuiopasdfghjklzxcvbnm")
new_list = []


def int_func(text_1):
    count = 0
    text_1 = text_1.split()
    for i in range(0, len(text_1)):
        for x in text_1[i]:
            if x in alphabet:
                count += 1
                if count == len(text_1[i]):
                    new_list.append(text_1[i])
                    count = 0
            else:
                count = 0

                break
    if new_list == []:
        return f"Строка не соответвует условиям, вводить нужно только латинские буквы нижнего регистра"
    else:
        input_text = ' '.join(new_list)
        result = input_text.title()
        return result


print(int_func(input("Введите любой текст: ")))
