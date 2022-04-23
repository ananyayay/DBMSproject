import mysql.connector as conn

class DataBase():
    def __init__(self) -> None:
        self.db = conn.connect(
            host = "localhost",
            user = "root",
            passwd = "13373301",
            database = "owla"
        )
        self.cursor = self.get_cursor()
    
    def get_cursor(self):
        return self.db.cursor()

    def get_vals(self, tablename):
        cur = self.cursor
        cur.execute(f"SELECT * FROM {tablename};")
        res = cur.fetchall()
        return res