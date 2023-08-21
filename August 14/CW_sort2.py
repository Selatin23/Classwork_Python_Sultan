# сортировка "выборкой"

user_in = input("Введите список цифр через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: int(x), user_in))

n = len(the_list)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if the_list[j] < the_list[min_index]:
            min_index = j
    the_list[i], the_list[min_index] = the_list[min_index], the_list[i]

print(the_list)
