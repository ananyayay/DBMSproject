from flask import Flask, redirect, render_template, request, url_for
from owla import owla_connector as oc

app = Flask(__name__)
db = oc.DataBase()

@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/admin_login.html", methods = ["GET", "POST"])
def admin_login():
    if request.method=="POST":
        ausers = db.get_admin_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(ausers, (usern, pw))
        if (usern, pw) in ausers:
            return render_template("admin_home.html")
        else:
            return render_template("loginfailed.html")
    return render_template("admin_login.html")

@app.route("/customer_login.html", methods = ["GET", "POST"])
def customer_login():
    if request.method=="POST":
        cusers = db.get_customer_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(cusers, (usern, pw))
        if (usern, pw) in cusers:
            return redirect(url_for("customer_home"))
        else:
            return render_template("loginfailed.html")
    return render_template("customer_login.html")

@app.route("/driver_login.html", methods = ["GET", "POST"])
def driver_login():
    if request.method=="POST":
        dusers = db.get_driver_users()
        usern = request.form["emailinput"]
        pw = request.form["passwordinput"]
        print(dusers, (usern, pw))
        if (usern, pw) in dusers:
            return render_template("driver_home.html")
        else:
            return render_template("loginfailed.html")
    return render_template("driver_login.html")

@app.route("/loginfailed.html")
def loginfailed():
    return render_template("loginfailed.html")

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
    if request.method=="POST":
        ridetype = request.form["ride"]
        cartype = request.form["cartype"]
        pickup = request.form["pickup"]
        drop = request.form["drop"]
        when = request.form["when"]
        db.insert_searchcabs(ridetype, pickup, drop, cartype)
        drivs = db.nearby_drivers(ridetype, pickup, cartype)
        d_id = drivs[0][0]
        deets = db.get_dr_details(d_id)
        db.insert_booking(d_id, when, pickup, drop, ridetype)
        books = db.get_booking()
        b_id = books[-1][0]
        db.insert_trip(b_id, pickup, drop)
        trip = db.get_trip()
        return booking(drivs, deets, [books[-1]], [trip[-1]])

    return render_template("customer_home.html")

@app.route("/add_location.html", methods = ["GET", "POST"])
def add_location():
    if request.method == "POST":
        street = request.form["streetinput"]
        locality = request.form["localityinput"]
        city = request.form["cityinput"]
        state = request.form["stateinput"]
        pincode = request.form["pincodeinput"]
        db.insert_location(street, locality, city, state, pincode)
        db.insert_savedplaces()
    return render_template("add_location.html")

@app.route("/driver_home.html", methods = ["GET", "POST"])
def driver_home():
    if request.method == "POST":
        if "first" in request.form:
            curr_ride = db.get_current_ride()
            curr_ride = [curr_ride[-1]]
            return table_template(curr_ride)
        elif "second" in request.form:
            past_books = db.get_past_bookings()
            return table_template(past_books)
        elif "third" in request.form:
            past_trips = db.get_past_trips()
            return table_template(past_trips)
    return render_template("driver_home.html")

@app.route("/yourvehicles.html", methods = ["GET", "POST"])
def get_vehicles():
    vehics = db.your_vehicles()
    return render_template("yourvehicles.html", row1 = vehics)

@app.route("/yourprofile.html", methods = ["GET", "POST"])
def yourprofile():
    prof = db.your_profile()
    return render_template("yourprofile.html", row1 = prof)

@app.route("/booking.html")
def booking(drivs, dets, book, trip):
    if request.method=="POST":
        paymode = request.form["modeinput"]
        amt = request.form["amountinput"]
        print(paymode, amt)
    return render_template("booking.html", row1 = drivs, row2 = dets, row3 = book, row4 = trip)

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