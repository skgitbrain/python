eng_rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("txttask_4.txt", "r", encoding="utf-8") as f:
    for i in f:
        if i.split()[0] in eng_rus_dic:
            with open("txttask_4_rus.txt", "a", encoding="utf-8", newline='') as f_rus:
                print(eng_rus_dic[i.split()[0]] + " " + i.split()[1] + " " + i.split()[2], file=f_rus)
