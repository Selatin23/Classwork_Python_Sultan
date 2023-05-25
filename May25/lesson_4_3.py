#задача 7
user_usb = input("Укажите объем флешки в гб:")
user_usb_file = input("Укажите размер файла в Мб:")

try:
    user_usb = int(user_usb)
    user_usb_file = int(user_usb_file)

except ValueError:
    message = "Ошибка! Вы ввели текст."

else:
    memory_1_gb = 1024
    usb_memory = user_usb * memory_1_gb
    file_copy_in_usb = usb_memory / user_usb_file
    template = "%d копий данного файла поместится на флешки."
    message = template % file_copy_in_usb

print(message)

