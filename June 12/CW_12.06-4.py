class Kettle():
    material = ""
    color = ""
    volume = 0
    water = 0

    def __init__ (self, material, color='red', volume=1):
        self.material = material
        self.color = color
        self.volume  = volume
    
    def fill (self, liters=None):
        if liters is None:
            self.water = self.volume
        elif self.water + liters > self.volume:
            extra_water = self.water + liters - self.volume
            print(f"Вылилось {extra_water} л")
            self.water = self.volume
        else:
            self.water = self.water + liters
        print(f'Теперь в чайнике {self.water} л')

my_kettle = Kettle("steel", "red", 1.7)
#other_kettle = Kettle("wood", "gray", 18)
#third_kettle = Kettle("plastic")
#print(my_kettle.material)
my_kettle.fill(0.7)
my_kettle.fill(0.7)
my_kettle.fill(0.7)
my_kettle.fill(0.7)