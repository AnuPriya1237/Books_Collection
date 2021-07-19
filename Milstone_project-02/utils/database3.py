import json
""" concerned with storing and retrieving books from json file.
json file format

[
{
"name":"mc furry"
"author":"gcjdsg"
"read":True
}
]
"""

book_file = 'book.json'

def create_book_table():
    with open(book_file,'w') as file:
        json.dump([], file)



def add_books(name, author):
    books = get_all_books()
    books.append({'name':name,'author':author,'read':False})
    _save_books(books)



def _save_books(books): #'_' underscore functions(function name strating with'_' are private functions in python
    with open(book_file,'w') as file:
        json.dump(books, file)



def get_all_books():
    with open(book_file,'r') as file:
        return json.load(file)


def to_read_books(book):
    books = get_all_books()
    for b in books:
        if b['name'] == book:
            b['read'] = True
    _save_books(books)



def to_delete_books(book):
    books = get_all_books()
    bookie = [ b for b in books if b['name'] != book]
    _save_books(bookie)

