#Main program

import ui, datastore, datamanipulation
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        remove_unread()

    elif choice == '6':
        rate_book()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def handle_sort_choice(sort_choice):

    if sort_choice == '1':
        ui.message("Sorted by author: ")

    elif sort_choice == '2':
        ui.message("Sorted by title: ")

    elif sort_choice == '3':
        choice = ui.display_menu_get_choice()
        handle_choice(choice)

    else:
        ui.message('Please enter a valid selection')

        
def s_title(book):
    return book.title

  
def s_author(book):
    return book.author


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)
    if len(unread) > 0:
        sort_choice = ui.display_sort_options()
        handle_sort_choice(sort_choice)
        if sort_choice == '1':
            s_list = sorted(unread, key=s_author)
            ui.show_list(s_list)
        elif sort_choice == '2':
            s_list = sorted(unread, key=s_title)
            ui.show_list(s_list)

            
def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)
    if len(read) > 0:
        sort_choice = ui.display_sort_options()
        handle_sort_choice(sort_choice)
        if sort_choice == '1':
            s_list = sorted(read, key=s_author)
            ui.show_list(s_list)
        elif sort_choice == '2':
            s_list = sorted(read, key=s_title)
            ui.show_list(s_list)

            
def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datamanipulation.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datamanipulation.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def remove_unread():
    '''Fetch and remove book from wishlist'''

    book_id = ui.ask_for_book_id()
    for book in datastore.book_list:
        if book_id == book_id and book.read == False:
            datamanipulation.remove_book(book_id)

def rate_book():
    '''Get rating from user, edit datastore, display book with rating or error'''

    book_id = ui.ask_for_book_id()
    book_rating = ui.ask_for_book_rating()
    if datamanipulation.set_rating(book_id, book_rating):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
