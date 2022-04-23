import mysql.connector as conn

class DataBase():
    def __init__(self) -> None:
        self.db = conn.connect(
            host = "localhost",
            user = "root",
            passwd = "13373301",
            database = "testdb"
        )
        self.cursor = self.get_cursor()
    
    def get_cursor(self):
        return self.db.cursor()

    def insert_vals(self, name, email):
        cur = self.cursor
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))

    def get_vals(self):
        cur = self.cursor
        cur.execute("SELECT * FROM users;")
        res = cur.fetchall()
        return res