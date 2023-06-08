#2. Пользователь ввел число, а на экран вывелись все числа от введенного до 0.
user_number = input("Введите число: ")

try:
    user_number = int(user_number)

except ValueError:
    user_number = None

if user_number == None:
    print("Ошибка!")

else:
    if user_number >= 0:
        for i in range(user_number, -1, -1):
            print(i)
    else:
        for i in range(user_number, 1):
            print(i)


