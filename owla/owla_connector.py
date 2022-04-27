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
        cur.execute(f"CREATE VIEW getval AS SELECT * FROM {tablename};")
        cur.execute("SELECT * FROM getval;")
        res = cur.fetchall()
        return res
    
    def get_wallet(self):
        cur = self.cursor
        q1 = []
        q2 = []
        cur.execute("CREATE VIEW walletview AS SELECT balance FROM olamoneyaccount WHERE customer_id=1;")
        cur.execute("SELECT * FROM walletview;")
        q1 = cur.fetchall()
        cur.execute("CREATE VIEW walletviewtransac as SELECT amount, timeoftransaction FROM transactions, olamoneyaccount WHERE olamoneyaccount.olamoneyaccount_id=1;")
        cur.execute("SELECT * FROM walletviewtransac;")
        q2 = cur.fetchall()
        cur.execute("DROP VIEW walletview;")
        cur.execute("DROP VIEW walletviewtransac;")
        return (q1, q2)
    
    def get_rides(self):
        cur = self.cursor
        q1, q2, q3, q4 = [], [], [], []
        cur.execute("CREATE VIEW ride1 AS SELECT from_location, to_location, timeofbooking, ridetype, status, reason, cancelledby, penalty from booking, cancelledrides WHERE booking.customer_id=1 AND booking.status='cancelled' and cancelledrides.booking_id=booking.booking_id;")
        cur.execute("SELECT * FROM ride1;")
        q1 = cur.fetchall()
        cur.execute("CREATE VIEW ride2 AS SELECT from_location, to_location, timeofbooking, ridetype, status, vehicle_type, duration_hrs, distance_km from booking, rentalpackages WHERE booking.customer_id=1 AND rentalpackages.package_id=booking.package_id;")
        cur.execute("SELECT * FROM ride2;")
        q2 = cur.fetchall()
        cur.execute("CREATE VIEW ride3 AS SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype='shared';")
        cur.execute("SELECT * FROM ride3;")
        q3 = cur.fetchall()
        cur.execute("CREATE VIEW ride4 AS SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype='outstation';")
        cur.execute("SELECT * FROM ride4;")
        q4 = cur.fetchall()
        cur.execute("DROP VIEW ride1;")
        cur.execute("DROP VIEW ride2;")
        cur.execute("DROP VIEW ride3;")
        cur.execute("DROP VIEW ride4;")
        return(q1, q2, q3, q4)

    def get_saved_locations(self):
        cur = self.cursor
        q1 = []
        cur.execute("CREATE VIEW savedlocs AS SELECT * FROM location WHERE location_id=(SELECT location_id FROM savedplaces WHERE customer_id= 1);")
        cur.execute("SELECT * FROM savedlocs;")
        q1 = cur.fetchall()
        cur.execute("DROP VIEW savedlocs;")
        return q1

    def query_1(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query1 AS SELECT COUNT(*) as searches_that_resulted_in_bookings FROM search WHERE booking_id IS NOT NULL;"""
        )
        cur.execute("SELECT * FROM query1;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query1;")
        return res

    def query_2(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query2 AS SELECT street, locality, city, state, pincode from location WHERE location_id = (SELECT location_id AS most_saved_location FROM savedplaces GROUP BY location_id ORDER BY COUNT(*) DESC LIMIT 1);"""
        )
        cur.execute("SELECT * FROM query2;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query2;")
        return res

    def query_3(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query3 AS SELECT * FROM drivers ORDER BY rating DESC LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query3;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query3;")
        return res

    def query_4(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query4 AS SELECT * FROM drivers WHERE noofratings>80 ORDER BY rating DESC LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query4;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query4;")
        return res

    def query_5(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query5 AS SELECT * FROM drivers ORDER BY earning LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query5;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query5;")
        return res

    def query_6(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query6 AS SELECT customers.customer_id,name,contact,emailid FROM customers,booking WHERE customers.customer_id = booking.customer_id and shared_id = (SELECT shared_id FROM booking WHERE customer_id = 25);"""
        )
        cur.execute("SELECT * FROM query6;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query6;")
        return res

    def query_7(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query7 AS SELECT * FROM payment WHERE trip_id = 1;"""
        )
        cur.execute("SELECT * FROM query7;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query7;")
        return res

    def query_8(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query8 AS SELECT driver_id, drivers.vehicle_id, name, contact, license FROM drivers, search, vehicles WHERE search.search_id= 101 and drivers.vehicle_id = vehicles.vehicle_id and search.from_location = vehicles.currentlocation_id and search.vehicle_type = vehicles.type;"""
        )
        cur.execute("SELECT * FROM query8;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query8;")
        return res

    def query_9(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query9 AS SELECT driver_id, name, contact, earning from drivers d1 WHERE 2 = (SELECT COUNT(DISTINCT(d2.earning)) FROM drivers d2 WHERE d2.earning>d1.earning);"""
        )
        cur.execute("SELECT * FROM query9;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query9;")
        return res

    def query_10(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query10 AS SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;"""
        )
        cur.execute("SELECT * FROM query10;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query10;")
        return res

    def query_11(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query11 AS SELECT type, COUNT(type) number_of_vehicles FROM vehicles GROUP BY type ORDER BY number_of_vehicles DESC;"""
        )
        cur.execute("SELECT * FROM query11;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query11;")
        return res

    def query_12(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query12 AS SELECT customers.customer_id, name,contact,emailid FROM customers WHERE EXISTS (SELECT * FROM olamoneyaccount WHERE olamoneyaccount.customer_id = customers.customer_id);"""
        )
        cur.execute("SELECT * FROM query12;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query12;")
        return res