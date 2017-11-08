
import sqlite3

'''To use the module, you must first create a Connection object that represents
   the database. Here the data will be stored in the example.db file.
   (You can also supply the special name :memory: to create a database in RAM.)

   Once you have a Connection, you can create a Cursor object and call its
   execute() method to perform SQL commands.
'''

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
         (id INTEGER, date TEXT, trans TEXT,
          symbol TEXT, qty REAL, price REAL)''')

# Insert a row
c.execute('''INSERT INTO stocks VALUES (1,'2017-11-08','BUY','BBY',135,67.24)''')

c.execute('''INSERT INTO stocks VALUES (2,'2017-11-08','BUY','ABC',552,88.13)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


'''
CREATE TABLE stocks
(id INTEGER, date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL);

INSERT INTO stocks VALUES (1,'2017-11-08','BUY','BBY',135,67.24);

INSERT INTO stocks VALUES (2,'2017-11-08','BUY','ABC',552,88.13);

UPDATE stocks
SET price = 125.99
WHERE id = 2;

ALTER TABLE stocks ADD COLUMN website TEXT;

UPDATE stocks
SET website = 'www.google.com'
WHERE id = 2;

# Deletes any rows where the website value is NULL(none exists)
DELETE FROM stocks WHERE website IS NULL; 


'''
