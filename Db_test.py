import sqlite3

def update_database(database):
    try:
        sqliteConnection = create_connection(database)
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

def insert_database(database):
    try:
        sqliteConnection = create_connection(database)
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

def display_database(database):
    try:
        sqliteConnection = create_connection(database)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT * FROM Stocks")

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    except sqlite3.Error as error:
        print("Failed to update sqlite table:", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")        

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        print("Connected to SQLite")
    except sqlite3.Error as e:
        print(e)
    return conn

def fetch_name(sqliteConnection,name):
    cur = sqliteConnection.cursor()
    cur.execute("SELECT * FROM Stocks WHERE Name = ?",[name])
    return cur.fetchall()

def fetch_volume(sqliteConnection,volume):
    cur = sqliteConnection.cursor()
    cur.execute("SELECT * FROM Stocks WHERE Volume = ?",[Volume])
    return cur.fetchall()

def get_date():
    from datetime import date
    print(date.today().strftime("%d/%m/%Y"))

if __name__ == '__main__':
    display_database('Holdings.db')
