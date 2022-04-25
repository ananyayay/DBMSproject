from flask import Flask, redirect, render_template, request
from owla import owla_connector as oc

app = Flask(__name__)
db = oc.DataBase()

@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/admin_login.html", methods = ["GET", "POST"])
def admin_login():
    return render_template("admin_login.html")

@app.route("/customer_login.html", methods = ["GET", "POST"])
def customer_login():
    if request.method == "POST":
        print(request.get_json())
    return render_template("customer_login.html")

@app.route("/driver_login.html", methods = ["GET", "POST"])
def driver_login():
    return render_template("driver_login.html")

@app.route("/admin_home.html", methods = ["GET", "POST"])
def admin_home():
    return render_template("admin_home.html")

@app.route("/customer_home.html", methods = ["GET", "POST"])
def customer_home():
    return render_template("customer_home.html")

@app.route("/table_template.html")
def olamoney_table():
    olamoney_wallet = db.get_vals("olamoneyaccount")
    return render_template("table_template.html", rows = olamoney_wallet)

@app.route("/admin_queries/query_1.html")
def query_1():
    query1 = db.query_1()
    return render_template("query_1.html", rows = query1)

@app.route("/query_2.html")
def query_2():
    query2 = db.query_2()
    return render_template("query_2.html", rows = query2)

@app.route("/query_3.html")
def query_3():
    query3 = db.query_3()
    return render_template("query_3.html", rows = query3)

@app.route("/query_4.html")
def query4():
    query4 = db.query_4()
    return render_template("query_4.html", rows = query4)

@app.route("/query_5.html")
def query5():
    query5 = db.query_5()
    return render_template("query_5.html", rows = query5)

@app.route("/query_6.html")
def query6():
    query6 = db.query_6()
    return render_template("query_6.html", rows = query6)

@app.route("/query_7.html")
def query7():
    query7 = db.query_7()
    return render_template("query_7.html", rows = query7)

@app.route("/query_8.html")
def query8():
    query8 = db.query_1()
    return render_template("query_8.html", rows = query8)

@app.route("/query_9.html")
def query_9():
    query9 = db.query_9()
    return render_template("query_9.html", rows = query9)

@app.route("/query_10.html")
def query_10():
    query10 = db.query_10()
    return render_template("query_10.html", rows = query10)

@app.route("/query_11.html")
def query_11():
    query11 = db.query_11()
    return render_template("query_11.html", rows = query11)

@app.route("/query_12.html")
def query_12():
    query12 = db.query_12()
    return render_template("query_12.html", rows = query12)

if __name__ == "__main__":
    app.run(debug = True)