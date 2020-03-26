import sqlite3

class DB_Creator:

    db = "timetoolDB.sqlite"

    create_times = """
                  CREATE TABLE times IF NOT EXISTS (
                      TimeID integer PRIMARY KEY,
                      Start integer NOT NULL,
                      Stop integer NOT NULL,
                      CategoryID integer NOT NULL,
                      FOREIGN KEY (CategoryID) REFERENCES categories (CategoryID)
                  );
                  """

    create_categories = """
                  CREATE TABLE categories IF NOT EXISTS (
                      CategoryID integer NOT NULL PRIMARY KEY,
                      CategoryName varchar(40) NOT NULL
                  );        
                  """

    conn = None

    def create_connection(self, database, conn):
        conn = self.conn
        try:
            self.conn = sqlite3.connect(database)
            return conn
        except sqlite3.Error as error:
            print(error),
        return conn


    def create_table(self, conn, orders):

        try:
            c = conn.cursor()
            c.execute(orders)
            conn.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Error:", error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("Connection closed.")

    def create_database(self):
        conn = create_connection(self.db, self.conn)
        if conn is not None:
            create_table(self.conn, self.create_times)
            create_table(self.conn, self.create_categories)
        else:
            print("Something went wrong, conn = None?")

        creator = DB_Creator()
        creator.create_database()