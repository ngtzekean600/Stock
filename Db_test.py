import sqlite3

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
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

updateSqliteTable()

def create_connection(db_file):
    from sqlite3 import Error
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite")
    except Error as e:
        print(e)
    return conn

def select_all_stocks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Stocks")

    rows = cur.fetchall()

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
