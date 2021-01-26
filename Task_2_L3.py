def user_info(name, suname, birth_year, city, email, phone):
    return f'{name} {suname} год рождения {birth_year}, проживающий в городе {city}, контакты: {email}, {phone}'


print(user_info(name="Игорь", suname="Петров", birth_year=1993, city="Москва", email="test@mail.ru",
                phone="+74991309283"))
