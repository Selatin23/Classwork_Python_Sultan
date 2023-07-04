
book = open("./task_1.txt", encoding="utf-8")
text = book.read()
book.close()

print(text)

user_input_new_word = input("Введите новое слово: ")
user_input_old_word = input("На какое слово хотите заменить: ")

index = text.find(user_input_old_word)
while index != -1:
    replaced_word = text[index:index + len(user_input_old_word)]
    if replaced_word[0].isupper():
        new_word = user_input_new_word.upper()
    elif replaced_word[0].isupper():
        new_word = user_input_new_word.capitalize()
    else:
        new_word = user_input_new_word.lower()
    text = text[:index] + text[index:index + len(user_input_old_word)].replace(user_input_old_word, new_word) + text[index + len(user_input_old_word):]
    index = text.find(user_input_old_word, index + len(new_word))

print(text)

