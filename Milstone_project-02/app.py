import utils.database3
user_choice =""" 
choices:-
'a' to add new book
'l' to list all books
'r' to mark a book as read
'd' to delete book
'q' to exit


enter your choice:
"""

def menu():
    utils.database3.create_book_table()
    user_input = input(user_choice)

    while user_input !='q':
        if user_input == 'a':
            prompt_add_books()
        elif user_input =='l':
            prompt_list_books()
        elif user_input == 'r':
            prompt_to_read()
        elif user_input == 'd':
            to_delete()
        else:
            print('unknown input!')

        user_input = input(user_choice)


def prompt_add_books():
    name = input('enter book name:')
    author = input('enter author name:')
    utils.database3.add_books(name, author)

def prompt_list_books():
    books = utils.database3.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']},read:{book['read']}")



""" 2nd way of writing this

def prompt_list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read] else 'NO'
        #(above line is same as) read = 'YES' if book['read] is True  else 'NO'
        print(f"{book['name']} by {book['author']},read:{book['read']}")


"""

def prompt_to_read():
    movie_name = input('movie name you want to mark as read:')
    utils.database3.to_read_books(movie_name)

def to_delete():
    movie_name = input('movie name you wanna delete:')
    utils.database3.to_delete_books(movie_name)





menu()