from functools import reduce

f = open("txttask_5.txt", "w", encoding="utf-8")
f.write("1 2 3 4 5 6 7 8 9")
f = open("txttask_5.txt", "r", encoding="utf-8")
y = f.readline().split()
sum = reduce(lambda a, b: int(a) + int(b), y)
print(sum)
f.close()
