from random import randint
# Person, Ticket, Kassa, Train

class Person:
    balance = 0
    iin = 0
    birth_date = ""
    first_name = ""
    last_name = ""
    ticket = False

    def __init__(self, name, last_name, birth_date):
        self.first_name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.iin = randint(100000000000, 999999999999)

    def show_info(self):
        info = f"""Человек: {self.first_name} {self.last_name},
        Дата рождения: {self.birth_date},
        ИИН: {self.iin}, денег: {self.balance}"""
        print(info)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0


class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    wagon = 0
    seat = 0
    datetime = ""
    passenger: Person = False

    def __init__(self, train_id, source, destination, datetime, person):
        self.train_id = train_id
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.passenger = person
        self.number = randint(100000, 999999)
        self.wagon = randint(1, 12)
        self.seat = randint(1, 32)

    def show(self):
        info = f"""Билет номер {self.number}:
        {self.source} - {self.destination}
        Отправление: {self.datetime},
        Поезд № {self.train_id}, вагон {self.wagon}, место {self.seat}
        Пассажир: {self.passenger.first_name} {self.passenger.last_name},
             ИИН: {self.passenger.iin}, {self.passenger.birth_date} г.р."""
        print(info)


class Kassa:
    balance = 0


    def get_price(self, source, destination):
        price = (len(source) + len(destination))*1000
        return price

    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.balance += money
            ticket = Ticket(train.number, source, destination, train.datetime, passenger)
            passenger.ticket = ticket
            return True
        else:
            return False

class Train:
    source = None
    destination = None
    datetime = None
    number = None

    def __init__(self, sourse, destination, datetime):
        self.source = sourse
        self.destination = destination
        self.datetime = datetime    
        self.number = randint(1, 100)

    def go(self, passenger):
        if passenger.ticket:
            if passenger.ticket.train_id == self.number and \
                passenger.ticket.datetime == self.datetime:
                    print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
                    passenger.ticket = False

dude = Person("Ilon", "Kask", "1994-06-25")
dude.earn(25000)
dude.pay(3500)
dude.show_info()

tmp_ticket = Ticket(23, "Алматы", "Ташкент", "2023-06-16 07:59", dude)

kassa = Kassa()

tmp_train = Train('Алматы', "Анталия", '2023-06-16 20:00')
kassa.buy_ticket(dude, 'Алматы', 'Анталия', tmp_train)
dude.ticket.show()
tmp_train.go(dude)


