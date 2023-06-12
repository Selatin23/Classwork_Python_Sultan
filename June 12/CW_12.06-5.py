class Kettle():
    material = ""
    color = ""
    volume = 0
    water = 0
    temprature = 0
    air = 0

    def __init__ (self, material, color='red', volume=1, temprature=0):
        self.material = material
        self.color = color
        self.volume  = volume
    
    def fill (self, liters=None):
        if liters is None:
            self.water = self.volume
        elif self.water + liters > self.volume:
            extra_water = self.water + liters - self.volume
            print(f'Вылилось {extra_water} л')
            self.water = self.volume
        else:
            self.water = self.water + liters
        print(f'Теперь в чайнике {self.water} л')

    def pour (self, liters=None):
        pass

    def boil (self, degrees=None):
        if degrees is None:
            self.air = self.temprature
        elif self.air + degrees > self.temprature:
            heating_air = self.air + degrees - self.temprature
            print(f'Нагрелось до {heating_air} C')
            self.air = self.temprature 
        else:
            self.air = self.air + degrees
        print(f'Температура чайника {self.air} С')

    def is_hot (self):
        return False

my_kettle = Kettle("steel", "red", 1.7, 1)
#other_kettle = Kettle("wood", "gray", 18)
#third_kettle = Kettle("plastic")
#print(my_kettle.material)
my_kettle.fill(0.7)
my_kettle.boil(10)