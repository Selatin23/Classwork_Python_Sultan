from random import randint

import kassa


class Train:
    source = None
    destination = None
    datetime = None
    number = None

    def __init__(self, kassa, sourse, destination, datetime) :
        self.source = sourse
        self.destination = destination
        self.datetime = datetime
        self.number = randint(1, 100)
        self.kassa = kassa
        kassa.register_train(self)

    def go(self, passenger):
        ticket  =  self.kassa.get_ticket(passenger, self.number, self.datetime):
        if ticket:
            print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
            kassa.delete_ticket(ticket)
        else:
            print("У вас билет не на этот поезд")

if __name__ == "__main__" :
    print("Train")
