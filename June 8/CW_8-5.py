result = 2+2*2
user_num = 0

while user_num != result:
    user_in = input("2 + 2 * 2 = ? ")
    try:
        user_num = int(user_in)
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз")

