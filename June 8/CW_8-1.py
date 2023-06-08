user_input = input("Сколько вывести смайликов?")
try:
    num = int(user_input)

except ValueError:
    num = None

if num is None or num < 0:
    print("Неправильный ввод, нужно положительное число!")

else:
    i = 0
    while i < num:
        print(":-)")
        i = i + 1

print("конец")