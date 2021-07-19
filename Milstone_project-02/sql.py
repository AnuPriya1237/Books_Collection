""" concerned with storing and retrieving books from database."""


import sqlite3

def create_book_table():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS anu(name text primary key,author text,read integer)')
    connection.commit()

    connection.close()

def add_books(name,author):
    connection  = sqlite3.connect('data.db')
    cursor = connection.cursor()

    connection.execute('INSERT INTO anu VALUES(?, ?, 0)', (name,author))
    connection.commit()

    connection.close()



def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM anu')


    """
    books = cursor.fetchall() #this gives all rows in the table
    #to view that in the form of a list like what we actually need
    
    """

    anu = [{'name':row[0], 'author':row[1], 'read':row[2]}for row in cursor.fetchall()]

    #It does not commit as here we are only reading books     connection.commit()

    connection.close()

    return anu




def to_read_books(bname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE anu SET read = 1 WHERE name = ?',(bname,))

    connection.commit()

    connection.close()


def to_delete_books(bname):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM anu WHERE name = ?',(bname,))

    connection.commit()

    connection.close()


