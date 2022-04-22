import mysql.connector as conn

db = conn.connect(
    host = "localhost",
    user = "root",
    passwd = "13373301",
    database = "testdb"
)

cur = db.cursor()

def insert_vals(name, email):
    cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
    db.commit()

def get_vals():
    cur.execute("SELECT * FROM users;")
    res = cur.fetchall()
    return res