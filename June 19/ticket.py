from random import randint
from person import Person

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

    def __repr__(self):
        info = f"""Билет {self.number}:{self.source} - {self.destination} на {self.train_id}@{self.datetime},"""
        return info

if __name__ == "__main__":
    print("Ticket")