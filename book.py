import datetime

class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1
    NO_DATE = datetime.date(1999, 9, 9)
    NO_RATING = "unrated"

    def __init__(self, title, author, read=False, dateRead=NO_DATE, rating=NO_RATING, id=NO_ID):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.dateRead = dateRead
        self.rating = rating
        self.id = id

    def set_id(self, id):
        self.id = id

    def set_dateRead(self, dateRead):
        self.dateRead = dateRead

    def set_rating(self, rating):
        self.rating = rating

    def __str__(self):
        read_str = 'no'
        dateRead_str = "N/A"
        if self.read:
            read_str = 'yes'
            dateRead_str = self.dateRead
            rating_str = self.rating
        id_str = self.id
        if id == -1:
            id_str = '(no id)'
        rating_str = self.rating

        template = 'id: {} Title: {} Author: {} Read: {} Date Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, dateRead_str, rating_str)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.dateRead == other.dateRead and self.rating == other.rating and self.id==other.id
