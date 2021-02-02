with open('txttask_2.txt', encoding="utf-8") as f:
    count = 0

    for i in f:
        line = i.split()
        count += 1
        print(f'Кол-во слов в строке {count} - {len(line)}')
print(f"Всего кол-во строк: {count}")
