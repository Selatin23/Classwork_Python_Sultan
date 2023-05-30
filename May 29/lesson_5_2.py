#elif
cost = input("Стоимость:")
cost = int(cost)
if cost < 1000:
    print("Скидок нет.")
elif cost < 2000:
    print("Скидка 2%.")
elif cost < 5000:
    print("Скидка 5%.")
else:
    print("Скидка 10%.")

print("Конец задача 1")

user_input = "Фенилэтиламин"

if 0 < len(user_input) <=5:
    print("Короткое слово")
elif 5 < len(user_input) <=10:
    print("Средней длины слово")
elif 10 < len(user_input) <=15:
    print("Длинное слово")
    if len(user_input) > 12:
        print("Больше 12 слов")
    else:
        print("Меньше 12 слов")
else:
    print("Это наверное на немецком")

print("Конец задача 2")