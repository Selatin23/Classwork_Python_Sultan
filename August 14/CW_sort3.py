# сортировка "пузьрьком"

user_in = input("Введите список цифр через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: float(x), user_in))

the_list = [12, 11, 9, 4, 0, 4, 3, 0]

k = 0

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(the_list) - 1):
        k = k + 1
        if the_list[i] > the_list[i + 1]:
            the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
            is_sorted = False

print(the_list)