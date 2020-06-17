import sqlite3

<<<<<<< HEAD
def update_database():
    try:
        sqliteConnection = create_connection('Holdings.db')
        cursor = sqliteConnection.cursor()

        name = 'OCBC'#input('What is your Stock: ')
        volume = 10 #int(input('What is your Volume: '))
        price = 5 #int(input('What is your price: '))
        cursor.execute('UPDATE Stocks SET Volume=?,Price=? where Name=?',[volume,price,name])
        sqliteConnection.commit()
        cursor.close()
        row = fetch_name(sqliteConnection,name)
        print("Record updated successfully:", row)
        
    except sqlite3.Error as error:
        print("Failed to update sqlite table:", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insert_database():
    try:
        sqliteConnection = create_connection('Holdings.db')
        cursor = sqliteConnection.cursor()

        name = 'DBS'#input('What is your Stock: ')
        volume = 5 #int(input('What is your Volume: '))
        price = 5 #int(input('What is your price: '))
        cursor.execute('INSERT INTO Stocks(Name,Volume,Price)\
                        VALUES(?,?,?)',[name,volume,price])
        sqliteConnection.commit()
        cursor.close()
        print("Record inserted successfully:", name)
        
    except sqlite3.Error as error:
        print("Failed to update sqlite table:", error)
=======
def update_stock():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update SqliteDb_developers set salary = 10000 where id = 4"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
>>>>>>> master
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

<<<<<<< HEAD
def create_connection(db_file):
=======
updateSqliteTable()

def create_connection(db_file):
    from sqlite3 import Error
>>>>>>> master
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite")
<<<<<<< HEAD
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all_database(conn):
=======
    except Error as e:
        print(e)
    return conn

def select_all_stocks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
>>>>>>> master
    cur = conn.cursor()
    cur.execute("SELECT * FROM Stocks")

    rows = cur.fetchall()
<<<<<<< HEAD
    for row in rows:
        print(row)

def fetch_name(sqliteConnection,name):
    cur = sqliteConnection.cursor()
    ID =1 
    cur.execute("SELECT * FROM Stocks WHERE Name = ?",[name])
    return cur.fetchall()

def fetch_volume(sqliteConnection,volume):
    cur = sqliteConnection.cursor()
    ID =1 
    cur.execute("SELECT * FROM Stocks WHERE Volume = ?",[Volume])
    return cur.fetchall()

def display_database():
    database = r"Holdings.db"
    conn = create_connection(database)
    with conn:
        print("test:")
        select_all_database(conn)

if __name__ == '__main__':
    update_database()
=======

    for row in rows:
        print(row)

def main():
    database = r"Holdings.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("test:")
        select_all_stocks(conn)

if __name__ == '__main__':
    main()
>>>>>>> master
