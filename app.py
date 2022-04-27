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
            print(db.query_1())
            return table_template(db.query_1())
        elif "second" in request.form:
            print(db.query_2())
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
    if request.method=="POST":
        ridetype = request.form["ride"]
        pickup = request.form["pickup"]
        drop = request.form["drop"]
        when = request.form["when"]
        
    return render_template("customer_home.html")

@app.route("/driver_home.html", methods = ["GET", "POST"])
def driver_home():
    return render_template("driver_home.html")

@app.route("/table_template.html")
def table_template(query):
    return render_template("table_template.html", rows = query)

@app.route("/yourwallet.html")
def yourwallet():
    q1, q2 = db.get_wallet()
    return render_template("yourwallet.html", row1 = q1, row2 = q2)

@app.route("/yourrides.html")
def yourrides():
    q1, q2, q3, q4 = db.get_rides()
    return render_template("yourrides.html", row1 = q1, row2 = q2, row3 = q3, row4 = q4)

@app.route("/savedlocations.html")
def savedlocations():
    q1 = db.get_saved_locations()
    return render_template("savedlocations.html", row1 = q1)

if __name__ == "__main__":
    app.run(debug = True)