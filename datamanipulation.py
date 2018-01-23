import datastore, datetime
from book import Book

def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list
    check_for_duplicates = []
    check_for_duplicates.append(book)

    for book in check_for_duplicates:
        if book not in datastore.book_list and book.read == True:
            book.id = generate_id()
            datastore.book_list.append(book)
            
        else:
            print('ALERT! BOOK HAS ALREADY BEEN READ')



def remove_book(book_id):
     '''remove book from wishlist'''
     global book_list
     global counter

     for book in datastore.book_list:

         if book.id == book_id and book.read == False:
             datastore.book_list.remove(book)
             print(book.title, 'has been removed from your wishlist')


def generate_id():
    counter = datastore.counter
    datastore.counter += 1
    return datastore.counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in datastore.book_list:

        if book.id == book_id:
            book.read = True
            book.dateRead = datetime.date.today()
            return True

    return False # return False if book id is not found

# def check_for_dups(book):
#     '''check to see if the user entry has already been read'''
#
#     global book_list
#     check_for_duplicates = []
#     check_for_duplicates.append(book)
#
#     for book in check_for_duplicates:
#         if book in datastore.book_list and book.read == True:
#             print('ALERT! BOOK HAS ALREADY BEEN READ')
#             datastore.book_list.remove(book)
#         else:
#             return book
