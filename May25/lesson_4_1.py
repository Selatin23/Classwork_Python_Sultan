user_input = input("Введите число:")

try:
    user_number = int(user_input)

except ValueError:
    result = "Ошибка! Вы ввели не число"

else:
    result = user_number ** 2

print("Квадрат числа:", result)
