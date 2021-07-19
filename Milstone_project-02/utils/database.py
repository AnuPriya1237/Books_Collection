"""concerned with storing and retrieving books from list"""

books = []

def add_books(name, author):
    books.append({'name': name,'author': author,'read': False})
    print(books)


def get_all_books():
    return books

def to_read_books(name):
    for book in books:
        if book['name'] == name:
            book['read']= True



""" one way
def to_delete_books(name):
    for book in books:
        if book['name'] == name:
            book.remove(name)
    print(books)
            """
#not removing it instead just adding all the books to new list  except the odd one(name)
""" 2nd way """
def to_delete_books(name):
    global books
    books = [book for book in books if book['name'] != name]    #keeping books global variable we can use same variable locally and globally too
    print(books)
