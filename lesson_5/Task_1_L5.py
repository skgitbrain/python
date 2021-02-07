my_file = open("my_file1.txt", 'a', encoding='utf-8')

while True:
    input_text = input("Введите текст для записи в файл: ")
    if input_text == '':
        break
    my_file.write(input_text + "\n")
my_file.close()
