import json

new_list = []
new_dic = {}
average_dic = {}
average_profit = 0
count = 0
with open("txttask_7.txt", "r", encoding="utf-8") as f:
    for i in f:
        profit = float(i.split()[2]) - float(i.split()[3])
        new_dic[i.split()[0]] = profit
        if profit > 0:
            average_profit += profit
            count += 1

    average_dic["average_profit"] = average_profit / count
    new_list.append(new_dic)
    new_list.append(average_dic)
with open("my_file.json", "w", encoding="utf-8") as json_f:
    json.dump(new_list, json_f, ensure_ascii=False, indent = 4)
