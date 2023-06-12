class Kettle ():
    material = "steel"
    color = "red"
    volume = 2.4

my_kettle = Kettle()
Kettle.material = "plastic"

print(my_kettle.material)
print(Kettle.material)