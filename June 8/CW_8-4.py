#4 Запросить 2 числа и найти общие делители.
user_num_1 = input ("Введите число:")
user_num_2 = input ("Введите число:")

try:
    user_num_1 = int(user_num_1)
    user_num_2 = int(user_num_2)

except ValueError:
    user_num_1 = None
    user_num_2 = None

if user_num_1 is None or user_num_2 is None:
    print("Неправильные числа!")

else:
    min_num = min(user_num_1, user_num_2)
    for i in range(1, min_num + 1):
        if user_num_1 % i == 0 and user_num_2 % i == 0:
            print(i)