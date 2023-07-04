
book = open("./book.txt", encoding="utf-8")
text = book.read()
book.close()

print(text)