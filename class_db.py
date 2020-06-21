import sqlite3
class database():
    def __init__(self):
        self.__database = 'Holdings.db'
    def create_connection(self):
        conn = None
        try:
            sqliteConnection = sqlite3.connect(self.__database)
            print("Connected to SQLite")
        except sqlite3.Error as error:
            print(error)
        return sqliteConnection
    def fetch_name(self,sqliteConnection,name,table):
        cur = sqliteConnection.cursor()
        cur.execute('SELECT * FROM '+table+' WHERE Name = ?',[name])
        return cur.fetchall()
    def fetch_volume(self,sqliteConnection,volume,table):
        cur = sqliteConnection.cursor()
        cur.execute('SELECT * FROM '+table+' WHERE Volume = ?',[Volume])
        return cur.fetchall()
    def get_date(self):
        from datetime import date
        print(date.today().strftime("%d/%m/%Y"))
    def in_database(self,name,table):
        sqliteConnection = self.create_connection()
        if self.fetch_name(sqliteConnection,name,table) != []:
            return True
        return False
    def close_database(self,sqliteConnection):
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        else:
            print('Connection had not been establised')
###############################################################################
class stocks(database):
    def __init__(self):
        super().__init__()
        self.__table = 'Stocks'
    def update_database(self,name,volume,price):
        if not self.in_database(name,self.__table):
            self.insert_database(name,volume,price)
            return
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute('UPDATE Stocks SET Volume=?,Price=? where Name=?',[volume,price,name])
            sqliteConnection.commit()
            cursor.close()
            print("Record updated successfully:", self.fetch_name(sqliteConnection,name,self.__table))
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)

    def insert_database(self,name,volume,price):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute('INSERT INTO Stocks(Name,Volume,Price)\
                            VALUES(?,?,?)',[name,volume,price])
            sqliteConnection.commit()
            cursor.close()
            print("Record inserted successfully:", self.fetch_name(sqliteConnection,name,self.__table))
            
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)

    def display_database(self):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute("SELECT * FROM " + self.__table)

            rows = cursor.fetchall()
            print('-----------------'+self.__table+'--------------------')
            for row in rows:
                print(row)
            print('------------------------------------------------------')
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)
###############################################################################
class scrapbook(database):
    def __init__(self):
        super().__init__()
        self.__table = 'Scrapbook'
    def insert_database(self,name,volume,price):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute('INSERT INTO {0}(Name,Volume,Price)\
                            VALUES(?,?,?)'.format(self.__table),[name,volume,price])
            sqliteConnection.commit()
            cursor.close()
            print("Record inserted successfully:", name)
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)
    def display_database(self):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute("SELECT * FROM " + self.__table)
            rows = cursor.fetchall()
            print('-----------------'+self.__table+'--------------------')
            for row in rows:
                print(row)
            print('------------------------------------------------------')
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)

if __name__ == '__main__':
    s = stocks()
    s.update_database('DD',20,1)
    s.display_database()
