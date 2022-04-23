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

@app.route("/customer_home.html", methods = ["GET", "POST"])
def customer_home():
    print("here")
    if request.method=="POST":
        customerData = request.form
        db.insert_vals()
        return render_template("customer_home.html")
    return render_template("customer_home.html")

@app.route("/olamoney_table.html")
def olamoney_table():
    olamoney_wallet = db.get_vals("olamoneyaccount")
    return render_template("olamoney_table.html", rows = olamoney_wallet)

if __name__ == "__main__":
    app.run(debug = True)