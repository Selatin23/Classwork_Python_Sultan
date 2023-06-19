from random import randint
from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []

    def get_price(self, source, destination):
        price = (len(source) + len(destination))*1000
        return price

    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.balance += money
            ticket = Ticket(train.number, source, destination, train.datetime, passenger)
            self.tickets.append(ticket)
            return True
        else:
            return False

    def get_ticket(self, passenger, train_number, datetime):
        for x in self.tickets:
            if x.passenger.iin == passenger.iin and x.traindin_id == train_number and x.datetime:
                return x

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)

if __name__ == "__main__":
    print("Kassa")