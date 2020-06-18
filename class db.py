import sqlite3
class database():
    def __init__(self):
        self.__database = 'Holdings.db'
    def create_connection(self):
        conn = None
        try:
            sqliteConnection = sqlite3.connect(self.__database)
            print("Connected to SQLite")
        except sqlite3.Error as e:
            print(e)
        return sqliteConnection

    def fetch_name(self,sqliteConnection,name):
        cur = sqliteConnection.cursor()
        cur.execute("SELECT * FROM Stocks WHERE Name = ?",[name])
        return cur.fetchall()

    def fetch_volume(self,sqliteConnection,volume):
        cur = sqliteConnection.cursor()
        cur.execute("SELECT * FROM Stocks WHERE Volume = ?",[Volume])
        return cur.fetchall()
    def get_date(self):
        from datetime import date
        print(date.today().strftime("%d/%m/%Y"))

class stocks(database):
    def __init__(self):
        super().__init__()
        self.__table = 'Stocks'
    def update_database(self):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()

            name = 'OCBC'#input('What is your Stock: ')
            volume = 10 #int(input('What is your Volume: '))
            price = 5 #int(input('What is your price: '))
            cursor.execute('UPDATE Stocks SET Volume=?,Price=? where Name=?',[volume,price,name])
            sqliteConnection.commit()
            cursor.close()
            print("Record updated successfully:", self.fetch_name(sqliteConnection,name))
            
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def insert_database(self):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()

            name = 'HiP'#input('What is your Stock: ')
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

    def display_database(self):
        try:
            sqliteConnection = self.create_connection()
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
class scrapbook():
    def __init__(self):
        pass

if __name__ == '__main__':
    s = stocks()
    s.display_database()
