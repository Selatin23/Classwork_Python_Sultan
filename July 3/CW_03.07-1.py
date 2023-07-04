my_name = '  ух Фарух  '

a = my_name.isdigit()

a = my_name.casefold()

a = my_name.center(20)

a = my_name.encode('koi8-r')

a = my_name.endswith("ух  ")

a = my_name.startswith("Фар")

a = my_name.expandtabs(20)

a = my_name.find("ар")

a = "Мама мыла {}".format("раму")

point = {'x': 4, 'y': -5}
a = '{y} {x}'.format_map(point)

my_list = ["mama", "ramy"]
a = "{} myla".format(my_list)

a = my_name.index('Ф')

a = my_name.istitle()

a = my_name.join(['1', '2', '3'])

a = my_name.strip()
a = my_name.rstrip()
a = my_name.lstrip()

print(a)