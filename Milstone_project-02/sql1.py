from typing import List,Dict,Union

""" concerned with storing and retrieving books from database."""

from  sql1_connections  import DatabaseConnection


ant = Dict[str, Union[str, int]]

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS anu(name text primary key,author text,read integer)')


def add_books(name : str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:

        cursor = connection.cursor()
        connection.execute('INSERT INTO anu VALUES(?, ?, 0)', (name, author))



def get_all_books() -> List[ant]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM anu')

        """
        books = cursor.fetchall() #this gives all rows in the table
        #to view that in the form of a list like what we actually need
    
        """

        anu = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

        # It does not commit as here we are only reading books     connection.commit()
        return anu


def to_read_books(bname) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE anu SET read = 1 WHERE name = ?', (bname,))




def to_delete_books(bname) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM anu WHERE name = ?', (bname,))




