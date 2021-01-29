from sys import argv

salary, hours, hourly_rate, bonus = argv


def salary(hours, hourly_rate, bonus):
    try:
        salary_1 = int(hours) * int(hourly_rate) + int(bonus)
        return salary_1
    except ValueError:
        return f"Необходимо водить только цифры!"


print(salary(hours, hourly_rate, bonus))
