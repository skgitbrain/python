list_1 = []

article = 0

while True:
    answer = input('Хотите добавить новый товар?')
    if answer == "да":
        list_1.insert(article, (article + 1, {}))
        product_name = input("Введите название товара")
        list_1[article][1]["название"] = product_name
        product_price = input("Введите цену товара")
        list_1[article][1]["цена"] = product_price
        product_quantity = input("Введите количество товара")
        list_1[article][1]["количество"] = product_quantity
        measure_unit = input("Введите единицу измерения")
        list_1[article][1]["ед."] = measure_unit
        article += 1

    elif answer == "нет":
        break
    else:
        print("Нужно ввести либо да либо нет")

list_product_name, list_product_price, list_product_quantity, list_measure_unit = [], [], [], []
for x in range(0, article):
    list_product_name.insert(x, list_1[x][1]["название"])
    list_product_price.insert(x, list_1[x][1]["цена"])
    list_product_quantity.insert(x, list_1[x][1]["количество"])
    list_measure_unit.insert(x, list_1[x][1]["ед."])

analytics = {"название": list_product_name, "цена": list_product_price, "количество": list_product_quantity,
             "ед.": list(set(list_measure_unit))}
print(analytics)
