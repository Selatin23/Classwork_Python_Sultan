# наследование
# полиморфизм
# инкапсуляция


class Car:
    def __init__(self, trade_mark, fuel_max, consumption):
        self.trade_mark = trade_mark
        self.fuel_max = fuel_max
        self.fuel_vol = 1
        self.consumption = consumption/100
        print(f"Поздравляем, теперь у вас есть новенький {trade_mark}!")

    def go(self, km):
        total = self.consumption * km
        if total > self.fuel_vol:
            print(f"Не хватает {total - self.fuel_vol} л. Не поедем! ")
        else:
            self.fuel_vol -= total
            print(f"Проехали {km} км! Осталось топлива {self.fuel_vol} л. ")

    def refuel(self, litres):
        print(f"Заправляем {litres} л.", end=" ")
        self.fuel_vol += litres
        if self.fuel_max < self.fuel_vol:
            pour_out = self.fuel_vol - self.fuel_max
            self.fuel_vol = self.fuel_max
            print(f"Вылилось {pour_out} л.", end=" ")
        print(f"Теперь уровень топлива {self.fuel_vol} л. ")


class Zaparozhets(Car):
    def __init__(self, color, speed):
        super().__init__('Zaparozhets', 50, 10)
        self.color = color
        self.speed = speed
        print(f"   И его цвет - {color}!")

    def go(self, km):
        super().go(km)
        time = km / self.speed
        print(f"Доехали за {time} часов")



class Truck(Car):
    def __init__(self, trade_mark, fuel_max, consumption, max_load):
        super().__init__(trade_mark, fuel_max, consumption)
        self.max_load = max_load
        self.current_load = 0

    def load(self, kg):
        self.current_load += kg
        print(f'Загрузили на {kg} кг. Общая загрузка {self.current_load} кг.')

    def unload(self, kg):
        if kg > self.current_load:
            print('У меня нет столько груза!')
        else:
            self.current_load -= kg
            print(f'Разгрузили {kg} кг, осталось {self.current_load}')

    def go(self, km):
        if self.current_load > self.max_load:
            print(f"Перегружен на {self.current_load - self.max_load} кг! Поездка невозможна!")
        else:
            super().go(km)

class Ramatruck(Truck):
    def __init__(self, color, speed, dog=True):
        super().__init__('RamaTruck', 500, 10, 20000)
        self.color = color
        self.dog = dog
        self.speed = speed
        print(f"    И его цвет {self.color}!")
        if dog:
            print("    У меня есть любимая собака!")
        else:
            print("    Вы не любите животных =((!")


zap = Zaparozhets("зелёный", 40)
zap.refuel(30)
zap.refuel(30)
zap.go(110)


gaz = Truck('Газель', 100, 20, 2000)
gaz.refuel(160)
gaz.load(3600)

gaz.go(400)
gaz.unload(1500)

ramaz = Ramatruck('Серобуромалиновый', 100)
ramaz.refuel(400)
ramaz.go(1200)

