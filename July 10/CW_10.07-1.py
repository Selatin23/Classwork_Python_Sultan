'''myfile = open('book.txt', 'r+', encoding='utf-8')
;;;text = myfile.read(50)
myfile.write('OLOLOOOO!')
text2 = myfile.read(50)
myfile.close()'''

# print(text)
# print(text2)

'''myfile = open('book.txt', 'a+', encoding='utf-8')
text = myfile.read(50)
myfile.write('OLOLOOOO!')
myfile.seek(0)
text2 = myfile.read(50)
myfile.close()

print(text)
print(text2)'''

with open('boo.txt', encoding='utf-8'') as myfile:
    text = myfile.read()