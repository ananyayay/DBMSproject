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
    return render_template("customer_login.html")

@app.route("/driver_login.html", methods = ["GET", "POST"])
def driver_login():
    return render_template("driver_login.html")

@app.route("/admin_home.html", methods = ["GET", "POST"])
def admin_home():
    if request.method=="POST":
        if "first" in request.form:
            return table_template(db.query_1())
        elif "second" in request.form:
            return table_template(db.query_2())
        elif "third" in request.form:
            return table_template(db.query_11())
        elif "fourth" in request.form:
            return table_template(db.query_12())
        elif "fifth" in request.form:
            return table_template(db.query_5())
        elif "sixth" in request.form:
            return table_template(db.query_4())
        elif "seventh" in request.form:
            return table_template(db.query_3())
    return render_template("admin_home.html")

@app.route("/customer_home.html", methods = ["GET", "POST"])
def customer_home():
    return render_template("customer_home.html")

@app.route("/table_template.html")
def table_template(query=None):
    if not query:
        query = db.get_vals("olamoneyaccount")
    return render_template("table_template.html", rows = query)

if __name__ == "__main__":
    app.run(debug = True)