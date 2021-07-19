"""concerned with storing and retrieving books from csv file.
csv file format
name,author,read
"""
book_file = 'book.txt'

def create_book_table():
    with open(book_file,'w') as file:
        pass #just to mark that file is there

def add_books(name, author):
    with open('book.txt','a') as file:
        file.write(f" name:{name}, author:{author} ,0\n")


def get_all_books():
    with open('book.txt','r') as file:
        line = file.readlines()
        lines = [li.strip() for li in line]
        data = lines.split(',')
        return  [
            {'name':data[0], 'author':data[1],'read':data[2] }
        ]

def to_read_books(bname):
    bookie = get_all_books()
    for book in bookie:
        if book['name'] == bname:
            book['read'] = '1'

    _save_books(bookie)

def _save_books(bookie):
    with open('book.txt','w') as file:
        for book in bookie:
            file.write(f"book:{book['name']},author:{book['author']},read:{book['read']}\n")


def to_delete_books(bname):
    bookie = get_all_books()
    books = [book for book in bookie if book['name'] != bname]
    _save_books(books)












