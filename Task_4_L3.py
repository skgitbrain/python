x = float(input("Введите действительное положительное число x: "))
y = int(input("Введите целое отрицательное число y: "))
def my_func(x,y):
    result = (x**1/(abs(y)))
    return result

print(my_func(4,2))