# Initializes database for expense tracking

import sqlite3

conn = sqlite3.connect('expense_tracking_DB.db') # connection to DB
c = conn.cursor()
c.execute("CREATE TABLE category (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
c.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
c.execute('''CREATE TABLE expense (id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    category_id INTEGER REFERENCES category NOT NULL,
    description TEXT,
    user_id INTEGER REFERENCES user NOT NULL,
    timestamp DATE NOT NULL)''')
conn.commit() # saves
conn.close()