some_words = input("Введите любое кол-во слов: ").split()

for ind, el in enumerate(some_words, 1):
    print(ind, el[0:10])
