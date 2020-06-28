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
        return date.today().strftime("%d/%m/%Y")
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
    def start_fk(self,cursor):
        cursor.execute("PRAGMA foreign_keys=ON")
######################################################################################################################
class stocks(database):
    def __init__(self):
        super().__init__()
        self.__table = 'Stocks'
    def update_database(self,name,code,average_cost=0,volume=0):
        if not self.in_database(name,self.__table):
            self.insert_database(name,code,average_cost,volume)
            return
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute('UPDATE Stocks SET Volume=?,AverageCost=? where Name=?',[volume,average_cost,name])
            sqliteConnection.commit()
            cursor.close()
            print("Record updated successfully:", self.fetch_name(sqliteConnection,name,self.__table))
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)

    def insert_database(self,name,code,average_cost=0,volume=0):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            cursor.execute('INSERT INTO Stocks(Name,Volume,Code,AverageCost)\
                            VALUES(?,?,?,?)',[name,volume,code,average_cost])
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
            print('{0} {1} {2} {3} {4}'.format('ID','Code','Volume','Price','Date'))
            for row in rows:
                print(row)
            print('------------------------------------------------------')
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)
#########################################################################################################################
class scrapbook(database):
    def __init__(self):
        super().__init__()
        self.__table = 'Scrapbook'
    def insert_database(self,code,volume=0,price=0):
        try:
            sqliteConnection = self.create_connection()
            cursor = sqliteConnection.cursor()
            self.start_fk(cursor)#Enforce foreign key
            cursor.execute('INSERT INTO Scrapbook(Code,Volume,Price,Date)\
                            VALUES(?,?,?,?)',[code,volume,price,self.get_date()])
            sqliteConnection.commit()
            cursor.close()
            print("Record inserted successfully:", code)
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
            print('{0:^5}{1:^5}{2:^10}{3:^5}{4:>10}'.format('ID','Code','Volume','Price','Date'))
            for row in rows:
                print('{0:^5}{1:^5}{2:^10}{3:^5}{4:>15}'.format(row[0],row[1],row[2],row[3],row[4]))
            print('------------------------------------------------------')
        except sqlite3.Error as error:
            print("Failed to update sqlite table:", error)
        finally:
            self.close_database(sqliteConnection)

if __name__ == '__main__':
    S=stocks()
    s=scrapbook()
    #S.update_database('Code','OCBC')
    #s.insert_database('Code')
    s.display_database()
