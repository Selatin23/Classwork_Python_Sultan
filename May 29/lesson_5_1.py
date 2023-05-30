print("1 == 1:", 1 == 1)
print("1 == 2:", 1 == 2)
print("1 != 1:", 1 != 1)
print("1 != 2:", 1 != 2)
print("1 > 1:", 1 > 1)
print("1 > 2:", 1 > 2)
print("not(1>2):", not(1 > 2))
print("0 < 3 < 8:", 0 < 3 < 8)

char = 'b'
print("'g' < char < 'z':", 'g' <= char <= 'z')

name1 = 'Виктория'
name2 = 'Юрий'
print("name1 < name2:", name1 <= name2)

name1 = 'Алёна'
name2 = 'Али'
print("Алёна < Али:", name1 <= name2)
print(ord('ё'))
print(ord('и'))
print(ord('A'))
print(ord('!'))
print(ord('\n'))
print(ord('\t'))

a=8
b=5
if a:
    print(a)
else:
    print(b)