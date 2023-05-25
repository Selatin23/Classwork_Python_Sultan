user_input = input("Введите число:")

try:
    user_number = int(user_input)

except ValueError as ex:
    result = "Ошибка! Вы ввели не число"
    print(ex)

except OSError:
    result = "Ошибка ОС!"

except TypeError:
    result = "Неверный тип данных"

else:
    result = user_number ** 2

print("Квадрат числа:", result)