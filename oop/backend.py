import sqlite3

class Database:

    def __init__(self):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)', (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM book')
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM book WHERE id=?', (id,))  # tak, ten przecinek w (item,) jest potrzebny xD
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
        conn.commit()
        conn.close()

if __name__=='__main__':
    # insert('The Sun', 'John Wick', 1969, 123451234)
    print(view())
    # s = search(author='John Smith')
    # update(s[0][0], s[0][1], s[0][2], 1111, s[0][4])
    # print(view())
