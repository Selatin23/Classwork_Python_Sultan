#задача 5
user_time_hour = input("Сколько часов? ")
user_time_min = input("Сколько минут? ")
user_time_sec = input("Сколько секунд? ")
template = "Осталось до конца дня %s секунд"

try:
    user_time_hour = int(user_time_hour)
    user_time_min = int(user_time_min)
    user_time_sec = int(user_time_sec)

except ValueError:
    result = "Ошибка! Вы ввели не число!"

else:
    hour_end = 23 - user_time_hour
    min_end = 59 - user_time_min
    sec_end = 59 - user_time_sec
    finish = (hour_end * 60 * 60) + (min_end * 60) + sec_end
    result = template % finish

print(result)