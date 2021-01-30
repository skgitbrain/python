from itertools import cycle
list_1 = [1,2,3,4]
c = 0
for el in cycle(list_1):
    if c > 10:
        break
    print(el)
    c += 1