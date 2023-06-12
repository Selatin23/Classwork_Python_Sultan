class Kettle():
    material = ""
    color = ""
    volume = 0
    water = 0

    def __init__ (self, material, color='red', volume=1):
        self.material = material
        self.color = color
        self.volume  = volume
    
    def fill (self, litters):
        self.water = self.water + litters
        print(f'Теперь в чайнике {self.water} л')

my_kettle = Kettle("steel", "red", 1.7)
other_kettle = Kettle("wood", "gray", 18)
third_kettle = Kettle("plastic")
print(my_kettle.material)
my_kettle.fill(1.6)
