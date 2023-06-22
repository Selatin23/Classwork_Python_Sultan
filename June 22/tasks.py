#1
numbers = input("Введите 5 чисел через запятую: ")
num_list = numbers.split(",")
print(num_list)

try:
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
print(num_list)

num_list = sum(num_list)
print(num_list)

num_list = num_list / 2
print(num_list)