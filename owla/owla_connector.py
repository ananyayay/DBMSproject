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
        cur.execute(f"CREATE VIEW AS SELECT * FROM {tablename};")
        res = cur.fetchall()
        return res
    
    def get_wallet(self):
        cur = self.cursor
        q1 = []
        q2 = []
        cur.execute("SELECT balance FROM olamoneyaccount WHERE customer_id=1;")
        q1 = cur.fetchall()
        cur.execute("SELECT amount, timeoftransaction FROM transactions, olamoneyaccount WHERE olamoneyaccount.olamoneyaccount_id=1;")
        q2 = cur.fetchall()
        return (q1, q2)
    
    def get_rides(self):
        cur = self.cursor
        q1, q2, q3, q4 = [], [], [], []
        cur.execute("SELECT from_location, to_location, timeofbooking, ridetype, status, reason, cancelledby, penalty from booking, cancelledrides WHERE booking.customer_id=1 AND booking.status='cancelled' and cancelledrides.booking_id=booking.booking_id;")
        q1 = cur.fetchall()
        cur.execute("SELECT from_location, to_location, timeofbooking, ridetype, status, vehicle_type, duration_hrs, distance_km from booking, rentalpackages WHERE booking.customer_id=1 AND rentalpackages.package_id=booking.package_id;")
        q2 = cur.fetchall()
        cur.execute("SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype='shared';")
        q3 = cur.fetchall()
        cur.execute("SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype='outstation';")
        q4 = cur.fetchall()
        return(q1, q2, q3, q4)

    def get_saved_locations(self):
        cur = self.cursor
        q1 = []
        cur.execute("SELECT * FROM location WHERE location_id=(SELECT location_id FROM savedplaces WHERE customer_id= 1);")
        q1 = cur.fetchall()
        return q1

    def query_1(self):
        cur = self.cursor
        cur.execute(
            """SELECT COUNT(*) as searches_that_resulted_in_bookings FROM search WHERE booking_id IS NOT NULL;"""
        )
        res = cur.fetchall()
        return res

    def query_2(self):
        cur = self.cursor
        cur.execute(
            """SELECT street, locality, city, state, pincode from location WHERE location_id = (SELECT location_id AS most_saved_location FROM savedplaces GROUP BY location_id ORDER BY COUNT(*) DESC LIMIT 1);"""
        )
        res = cur.fetchall()
        return res

    def query_3(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT * FROM drivers ORDER BY rating DESC LIMIT 10;"""
        )
        res = cur.fetchall()
        return res

    def query_4(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT * FROM drivers WHERE noofratings>80 ORDER BY rating DESC LIMIT 10;"""
        )
        res = cur.fetchall()
        return res

    def query_5(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT * FROM drivers ORDER BY earning LIMIT 10;"""
        )
        res = cur.fetchall()
        return res

    def query_6(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT customers.customer_id,name,contact,emailid FROM customers,booking WHERE customers.customer_id = booking.customer_id and shared_id = (SELECT shared_id FROM booking WHERE customer_id = 25);"""
        )
        res = cur.fetchall()
        return res

    def query_7(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT * FROM payment WHERE trip_id = 1;"""
        )
        res = cur.fetchall()
        return res

    def query_8(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT driver_id, drivers.vehicle_id, name, contact, license FROM drivers, search, vehicles WHERE search.search_id= 101 and drivers.vehicle_id = vehicles.vehicle_id and search.from_location = vehicles.currentlocation_id and search.vehicle_type = vehicles.type;"""
        )
        res = cur.fetchall()
        return res

    def query_9(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT driver_id, name, contact, earning from drivers d1 WHERE 2 = (SELECT COUNT(DISTINCT(d2.earning)) FROM drivers d2 WHERE d2.earning>d1.earning);"""
        )
        res = cur.fetchall()
        return res

    def query_10(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;"""
        )
        res = cur.fetchall()
        return res

    def query_11(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT type, COUNT(type) number_of_vehicles FROM vehicles GROUP BY type ORDER BY number_of_vehicles DESC;"""
        )
        res = cur.fetchall()
        return res

    def query_12(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW AS SELECT customers.customer_id, name,contact,emailid FROM customers WHERE EXISTS (SELECT * FROM olamoneyaccount WHERE olamoneyaccount.customer_id = customers.customer_id);"""
        )
        res = cur.fetchall()
        return res