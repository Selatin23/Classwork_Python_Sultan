#1
import random

num1 = random.randint(-100, 100)
num2 = random.randint(-100, 100)

begin = min(num1, num2)
end = max(num1, num2)
print(begin)
print(end)

generation = []
for i in range(10):
    num = random.randint(begin, end)
    generation.append(num)

print("Список случайных чисел:", generation)

#2

current_length = 1
max_length = 1

for i in range (1, len(generation)):
    if generation[i] >=  generation [i-1]:
         current_length = current_length + 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1

max_length = max(max_length, current_length)
print(max_length)

#3
names = ["Амир", "Султан", "Ильяс", "Гоги", "Абай", "Даная", "Асем", "Тимур"]
marks = [3,2,5,7,8,1,2,3]

res = list(zip(names, marks))

print(res)





