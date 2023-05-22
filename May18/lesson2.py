#1 Запросите у пользователя число, возведите это число во 2-ю степень и выведите на экран.
user_input = input("Введите число:")
user_int = int(user_input)

result = user_int ** 2
print("Результат:", result)

#2 Запросите у пользователя 2 числа и выведите среднее арифметическое этих чисел.
user_input1 = input("Введите число:")
user_input2 = input("Введите число:")
user_int1 = int(user_input1)
user_int2 = int(user_input2)

result = (user_int1 + user_int2) / 2
print("Результат:", result)

#3 Запросите у пользователя длину стороны квадрата и выведите площадь такого квадрата.
user_input = input("Длина стороны квадрата:")
user_int = int(user_input)

result = user_int * user_int
print("Результат:", result)

#4 Реализуйте конвертор из километров в мили (пользователь вводит километры, программа выводит мили). 1 км = 0,621371 миль.
user_input = input("КМ:")
user_int = int(user_input)
mile = 0.621371

result = user_int * mile
print("Результат мили:", result)

#5 Реализуйте калькулятор. Пользователь вводит два числа, а программа выводит результаты действий + - * / между этими числами.
user_input1 = float(input ("Введите первое число:"))
user_input2 = float(input ("Введите второе число:"))

add = user_input1 + user_input2
subtract = user_input1 - user_input2
multiply = user_input1 * user_input2
divide = user_input1 / user_input2
print("Сложение:", add)
print("Вычитание:", subtract)
print("Умножение:", multiply)
print("Деление:", divide)

#6 Пользователь вводит значения a и b для формулы a * x + b = 0, а программа считает и выводит значение x.
a = float(input("Введите значение a:"))
b = float(input("Введите значение b:"))
x = -b / a
print("Значение x:", x)

#7 Запросите у пользователя текущее время (часы и минуты) и выведите, сколько часов и минут осталось до следующего дня.
hour = int(input("Введите часы:"))
min = int(input("Введите минуты:"))

balancehour = 23 - hour1
balancemin = 60 - min
print(balancehour, ":", balancemin)

#8 Запросите у пользователя трехзначное число и выведите вторую цифру этого числа. Для решения задачи используйте оператор % (остаток от деления).

