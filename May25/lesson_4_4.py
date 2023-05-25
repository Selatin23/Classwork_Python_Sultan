user_number = input("Введите число: ")

try:
    number = int(user_number)

except ValueError:
    message = "Вы ввели не число!"

else:
    message = "Ваше число в:"
    message += "\n - двоичном виде: %s" % bin(number)
    message += "\n - восьмиричном виде: %s" % oct(number)
    message += "\n - шестнадцатиричном виде: %s" % hex(number)

print(message)
