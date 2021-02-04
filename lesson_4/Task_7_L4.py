def fact(num):
    fact_1 = 1
    for i in range(1, num + 1):
        fact_1 *= i
        yield fact_1


num = 4
for x in fact(num):
    print(x)
