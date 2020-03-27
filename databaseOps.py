import sqlite3
# import os ; print(os.getcwd())

class DB_orders_to_execute:

    def __init__(self):

        self.db = "timetool.db"

        self.create_times = """
             CREATE TABLE IF NOT EXISTS times (
                 TimeID integer PRIMARY KEY,
                 Start integer NOT NULL,
                 Stop integer NOT NULL,
                 CategoryID integer NOT NULL,
                 FOREIGN KEY (CategoryID) REFERENCES categories (CategoryID)
             );
                             """

        self.create_categories = """
             CREATE TABLE IF NOT EXISTS categories (
                 CategoryID integer NOT NULL PRIMARY KEY,
                 CategoryName varchar(40) NOT NULL
             );        
                                """

class DB_Operator:

    def __init__(self):

        self.Orders = DB_orders_to_execute()

    def connect(self, database):

        conn = None
        try:
            conn = sqlite3.connect(database)
        except sqlite3.Error as error:
            print(error)
        return conn

    def create_table(self, conn, orders):

        c = conn.cursor()
        c.execute(orders)
        conn.commit()
        c.close()

    def create_database(self):

        conn = self.connect(self.Orders.db)

        if conn is not None:
            self.create_table(conn, self.Orders.create_times)
            self.create_table(conn, self.Orders.create_categories)

        else:
            print("Something went wrong, see over connection")

        conn.close()

    def select(self, items):
        # item = ("tablename", 'ITEMNAME',)
        conn = self.connect(self.Orders.db)
        c = conn.cursor()
        c.execute('SELECT * FROM ?', items)
        results = c.fetchall()
        conn.close()
        return results



Damian = DB_Operator()
Damian.create_database()
