#1
def square(a):
    def tmp_square(s):
        return s*s
    return tmp_square(a)


print( square(4) )

#2
def square(num):
    def tmp_square(num):
        return num ** 2
    return tmp_square(num)

result = square(2)
print(result)

#3
def increment (num):
    num = num + 1    
    try:
        return increment(num)
    except RecursionError as error:
        print("\nПеребор", error)
        return 0
    
num = 2
result = increment (num)

print(result)
print(num)