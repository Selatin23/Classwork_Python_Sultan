from person import Person
from ticket import Ticket
from kassa import Kassa
from train import Train

if __name__ == "__main__":
    ilon = Person("Ilon", "Kask", "1994-06-25")
    ilon.earn(25000)
    ilon.show_info()

    alex = Person("Alex", "Boldwin", "1954-06-25")
    alex.earn(35000)
    alex.show_info()

    kassa = Kassa()
    train_to_chile = Train(kassa, 'Алматы', "Сантьяго", '2023-06-16 20:00')
    train_to_uruguay = Train(kassa, 'Алматы', "Монтевидео", '2023-06-16 09:00')

    kassa.buy_ticket(ilon, 'Алматы', 'Сантьяго', train_to_chile)
    kassa.buy_ticket(ilon, 'Алматы', 'Монтевидео', train_to_chile)

    kassa.buy_ticket(alex, 'Алматы', 'Сантьяго', train_to_chile)
    kassa.buy_ticket(alex, 'Алматы', 'Сантьяго', train_to_chile)

    print(kassa.tickets)
    train_to_chile.go(ilon)
    print(kassa.tickets)