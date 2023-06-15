class Book():
    author = "noname"
    title = "noname"
    pub_year = "1900"
    readed = False

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.pub_year = year

    def read(self):
        self.read = True
    
redbook = Book ("CD", "Sherlock", 1996)
bluebook = Book(year=1780, )