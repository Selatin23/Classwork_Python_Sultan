# сортировка "пузьрьком"

the_list_str = input("Введите список цифр через запятую: ")
the_list_str = the_list_str.split(',')

print(the_list_str)

the_list = list(map(lambda x: float(x), the_list_str))

print(the_list)

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(the_list) - 1):
        if the_list[i] > the_list[i + 1]:
            the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
            is_sorted = False

print(the_list)

            