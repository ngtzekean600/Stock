import sqlite3

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
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite")
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all_database(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Stocks")

    rows = cur.fetchall()
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
        select_all_database(conn)

def get_date():
    from datetime import date
    print(date.today().strftime("%d/%m/%Y"))

if __name__ == '__main__':
    get_time()
