import ini

config = ini.parse('config.ini')
print("Наша конфигурация: ")
print(config)

user_resp = input("Хотите изменить конфигурацию? (y/n): ")
if user_resp in "yYдД":
    user_section = input("В какой секции? ")
    if user_section in "debug, deploy, test":
        user_key = input("какой ключ хотите поменять?")
        if user_key in config:
            print(f"Значение для ключа '{user_key}': {value}")
        else:
            print(f"Ключ '{user_key}' не найден в словаре.")
