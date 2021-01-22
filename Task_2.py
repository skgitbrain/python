num = int(input("Введитe любое количество секунд: "))

hour = num // 3600
minute = (num // 60) % 60
seconds = num % 60

print('{:02}:{:02}:{:02}'.format(hour, minute, seconds))
