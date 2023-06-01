#1. функцию которая принимает 2 числа и возвращает меньшее из них.

def get_min(num1, num2):
    if num1 > num2:
        return num2
    else:
        return num1

result = get_min(6, -9)
print(result)

#2. функцию которая возводит переданное число в указанную степень.

def get_power(num, power):
    empowered = num ** power
    return empowered

result = get_power(3, 5)
print("Результат:", result)

#3. функцию которая принимает 2 числа и знак (+ - * /), считает пример и возвращает результат.
def calculator(num1, num2, sign):
    if sign == "+":
        result = num1 + num2
        return result
    
    elif sign == "-":
        result = num1 - num2
        return result
    
    elif sign == "*":
        result = num1 * num2
        return result
    
    else:
        result = num1 / num2
        return result

result = calculator(3, 7, "*")
print(result)

#4. 

def get_reminder(num1, num2):
    div_result = num1 // num2
    reminder = num1 - (div_result * num2)
    return reminder

result = get_reminder(11,4)
print("Остаток:", result)

'''
get_reminder(11,4)
    div_result = 2
    reminder = 11 - (2 * 4) = 8
    11 - 8 = 3
'''

#6 Написать функцию, которая принимает от 1 до 4 чисел и возвращает большее из них.
def get_max (num1, num2, num3, num4):
    if num1 > num2:
        return num1
    elif num2 > num3:
        return num2
    elif num3 > num4:
        return num3
    else:
        return num4
    
result = get_max(22, 8, 10, 19)
print(result)

#7

def show_multiply_table(num, i=1):
    print("%d x %d = %d" % (num, i, num*i))
    if i < 10:
        show_multiply_table(num, i+1)
    return

show_multiply_table(6)