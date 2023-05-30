#Задание 1
user_input = input("Введите число:")
user_input = int(user_input)

if user_input < 0:
    print("Отрицательное.")

elif user_input > 0:
    print("Положительное.")

else:
    print("Ноль")

print("Конец.")

#Задание 2
user_input = input("Введите свой возраст:")
user_input = int(user_input)

if user_input < 0:
    print("Вас еще нету.")

elif user_input < 120:
    print("Корректно")

else:
    print("Умер.")

print("Конец.")

#Задание 3
user_input = input("Enter number:")
#user_num = float(user_input)

#module = abs(user_num)

try: 
    user_num = float(user_input)

except ValueError:
    message = "Вы ввели неверное число."

else:
    message = "Ваш модуль %s" % user_num
    if user_num < 0:
        user_num = -user_num

print(message)

#Задание 4
user_input_hour = input("Введите часы:")
user_input_minute = input("Введите минуты:")
user_input_secund = input("Введите секунды:")

user_input_hour = int(user_input_hour)
user_input_minute = int(user_input_minute)
user_input_secund = int(user_input_secund)


if user_input_hour < 0 or user_input_hour > 24:
    print("Ошибка часы")
elif user_input_minute < 0 or user_input_minute > 60:
    print("Ошибка минуты")
elif user_input_secund < 0 or user_input_secund > 60:
    print("Ошибка секунды")
else:
    print("Все верно")

print("Конец.")

#Задание 5
user_input_x = input("Введите координаты точки x:")
user_input_y = input("Введите координаты точки y:")

user_input_x = int(user_input_x)
user_input_y = int(user_input_y)

if user_input_x > 0 and user_input_y > 0:
    print("Первая четверть")

elif user_input_x < 0 and user_input_y > 0:
    print("Вторая четверть")

elif user_input_x < 0 and user_input_y < 0:
    print("Третья четверть")

else:
    print("Четвертая четверть")

print("Конец.")

#Задание 1-2
number1_input = input("Введите первое число:")
number2_input = input("Введите второе число:")
symbol = input("Введите знак:")
message = "Вы ввели неккоректное значения чисел!"

try:
    number1 = float(number1_input)
    number2 = float(number2_input)

except ValueError:
    number1 = number2 = ""

else:
    if symbol in "+-*/":
        template = "%.2f %s %.2f = %.2f"
        if symbol == "+":
            result = number1 + number2
        elif symbol == "-":
            result = number1 - number2
        elif symbol == "*":
            result = number1 * number2
        elif symbol == "/":
            result = number1 / number2
        message = template % (number1, symbol, number2)

print("Ошибка!")

