import mysql.connector as conn
import datetime

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
        return (list(set(q1)), list(set(q2)))
    
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
        return (list(set(q1)), list(set(q2)), list(set(q3)), list(set(q4)))

    def get_saved_locations(self):
        cur = self.cursor
        q1 = []
        cur.execute("CREATE VIEW savedlocs AS SELECT l.street, l.locality, l.city, l.state, l.pincode FROM location AS l, customers AS c, savedplaces AS sp WHERE sp.customer_id=1 AND sp.location_id=l.location_id;")
        cur.execute("SELECT * FROM savedlocs;")
        q1 = cur.fetchall()
        cur.execute("DROP VIEW savedlocs;")
        return list(set(q1))

    def insert_searchcabs(self, ridetype, pickup, drop, vehicle_type):
        cur = self.cursor
        cur.execute("INSERT INTO search(customer_id, from_location, to_location, ridetype, vehicle_type) VALUES (1, %s, %s, %s, %s);", (pickup, drop, ridetype, vehicle_type))
        self.db.commit()

    def query_1(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query1 AS SELECT COUNT(*) as searches_that_resulted_in_bookings FROM search WHERE booking_id IS NOT NULL;"""
        )
        cur.execute("SELECT * FROM query1;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query1;")
        return list(set(res))

    def query_2(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query2 AS SELECT street, locality, city, state, pincode from location WHERE location_id = (SELECT location_id AS most_saved_location FROM savedplaces GROUP BY location_id ORDER BY COUNT(*) DESC LIMIT 1);"""
        )
        cur.execute("SELECT * FROM query2;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query2;")
        return list(set(res))

    def query_3(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query3 AS SELECT * FROM drivers ORDER BY rating DESC LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query3;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query3;")
        return list(set(res))

    def query_4(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query4 AS SELECT * FROM drivers WHERE noofratings>80 ORDER BY rating DESC LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query4;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query4;")
        return list(set(res))

    def query_5(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query5 AS SELECT * FROM drivers ORDER BY earning LIMIT 10;"""
        )
        cur.execute("SELECT * FROM query5;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query5;")
        return list(set(res))

    def query_6(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query6 AS SELECT customers.customer_id,name,contact,emailid FROM customers,booking WHERE customers.customer_id = booking.customer_id and shared_id = (SELECT shared_id FROM booking WHERE customer_id = 25);"""
        )
        cur.execute("SELECT * FROM query6;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query6;")
        return list(set(res))

    def query_7(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query7 AS SELECT * FROM payment WHERE trip_id = 1;"""
        )
        cur.execute("SELECT * FROM query7;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query7;")
        return list(set(res))

    def query_8(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query8 AS SELECT driver_id, drivers.vehicle_id, name, contact, license FROM drivers, search, vehicles WHERE search.search_id= 101 and drivers.vehicle_id = vehicles.vehicle_id and search.from_location = vehicles.currentlocation_id and search.vehicle_type = vehicles.type;"""
        )
        cur.execute("SELECT * FROM query8;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query8;")
        return list(set(res))

    def query_9(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query9 AS SELECT driver_id, name, contact, earning from drivers d1 WHERE 2 = (SELECT COUNT(DISTINCT(d2.earning)) FROM drivers d2 WHERE d2.earning>d1.earning);"""
        )
        cur.execute("SELECT * FROM query9;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query9;")
        return list(set(res))

    def query_10(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query10 AS SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;"""
        )
        cur.execute("SELECT * FROM query10;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query10;")
        return list(set(res))

    def query_11(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query11 AS SELECT type, COUNT(type) number_of_vehicles FROM vehicles GROUP BY type ORDER BY number_of_vehicles DESC;"""
        )
        cur.execute("SELECT * FROM query11;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query11;")
        return list(set(res))

    def query_12(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW query12 AS SELECT customers.customer_id, name,contact,emailid FROM customers WHERE EXISTS (SELECT * FROM olamoneyaccount WHERE olamoneyaccount.customer_id = customers.customer_id);"""
        )
        cur.execute("SELECT * FROM query12;")
        res = cur.fetchall()
        cur.execute("DROP VIEW query12;")
        return list(set(res))
    
    def get_current_bookings(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW current_bookings AS ;"""
        )
        cur.execute("SELECT * FROM current_bookings;")
        res = cur.fetchall()
        cur.execute("DROP VIEW current_bookings;")
        return list(set(res))
    
    def get_past_bookings(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW past_bookings AS ;"""
        )
        cur.execute("SELECT * FROM past_bookings;")
        res = cur.fetchall()
        cur.execute("DROP VIEW past_bookings;")
        return list(set(res))
    
    def get_past_trips(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW past_trips AS ;"""
        )
        cur.execute("SELECT * FROM past_trips;")
        res = cur.fetchall()
        cur.execute("DROP VIEW past_trips;")
        return list(set(res))
    
    def nearby_drivers(self, ridetype, pickup, cartype):
        cur = self.cursor
        if ridetype=="cityride":
            cur.execute(
                """CREATE VIEW nearbydr AS SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price FROM drivers, vehicles WHERE drivers.vehicle_id = vehicles.vehicle_id and %s = vehicles.currentlocation_id and vehicles.type = %s and vehicles.availability=1;""",
                (pickup, cartype)
            )
        elif ridetype=="shared":
            cur.execute(
                """CREATE VIEW nearbydr AS SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price FROM drivers, vehicles WHERE drivers.vehicle_id = vehicles.vehicle_id and %s = vehicles.currentlocation_id and vehicles.type = %s and vehicles.availability=1 and maxcapacity>1;""",
                (pickup, cartype)
            )
        elif ridetype=="rentals":
            cur.execute(
                """CREATE VIEW nearbydr AS SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price FROM drivers, vehicles WHERE drivers.vehicle_id = vehicles.vehicle_id and %s = vehicles.currentlocation_id and vehicles.type = %s and vehicles.availability=1 and rental=1;""",
                (pickup, cartype)
            )
        elif ridetype=="outstation":
            cur.execute(
                """"CREATE VIEW nearbydr AS SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price FROM drivers, vehicles WHERE drivers.vehicle_id = vehicles.vehicle_id and %s = vehicles.currentlocation_id and vehicles.type = %s and vehicles.availability=1 and interstatepermit=1;""",
                (pickup, cartype)
            )
        cur.execute("SELECT * FROM nearbydr;")
        res = cur.fetchall()
        cur.execute("DROP VIEW nearbydr;")
        return list(set(res))
    
    def get_dr_details(self, d_id):
        cur = self.cursor
        cur.execute(
            f"""CREATE VIEW deets AS SELECT drivers.name, drivers.contact, drivers.rating, drivers.tripscompleted, vehicles.numberplate, vehicles.brand, vehicles.model, vehicles.type, vehicles.fueltype FROM drivers, vehicles WHERE drivers.vehicle_id = vehicles.vehicle_id and drivers.driver_id = {d_id};""",
        )
        cur.execute("SELECT * FROM deets;")
        res = cur.fetchall()
        cur.execute("DROP VIEW deets;")
        return list(set(res))
    
    def insert_booking(self, d_id, when, pickup, drop, ridetype):
        cur = self.cursor
        if when=="now":
            cur.execute(
                """INSERT into booking (driver_id, customer_id, from_location, to_location, timeofbooking, ridetype, noofpassengers, isScheduled, status) values (%s, '1', %s, %s, %s, %s, '1', '0', 'booked');""",
                (d_id, pickup, drop, datetime.datetime.now().strftime("%H:%M:%S"), ridetype)
                )
        else:
            cur.execute(
                """INSERT into booking (driver_id, customer_id, from_location, to_location, timeofbooking, scheduledtime, ridetype, noofpassengers, isScheduled, status) values (%s, '1', %s, %s, %s, %s, %s, '1', '1', 'booked');""",
                (d_id, pickup, drop, datetime.datetime.now().strftime("%H:%M:%S"), datetime.datetime.strptime(when, "%H:%M:%S"), ridetype)
            )
        self.db.commit()
    
    def get_booking(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW showbooked AS SELECT booking.booking_id, drivers.name, drivers.contact, from_location, to_location, timeofbooking, scheduledtime, ridetype, noofpassengers, status FROM drivers, booking WHERE drivers.driver_id = booking.driver_id AND customer_id='1' AND booking.status='booked';"""
        )
        cur.execute("SELECT * FROM showbooked;")
        res = cur.fetchall()
        cur.execute("DROP VIEW showbooked;")
        return list(set(res))
    
    def insert_trip(self, b_id, pickup, drop):
        cur = self.cursor
        distance = abs(int(drop) - int(pickup))
        curr_time = datetime.datetime.now()
        td = datetime.timedelta(hours=distance/50)
        new_currtime = curr_time + td
        cur.execute(
            """INSERT into trip(booking_id, pickuplocation, droplocation, distance, starttime, endtime) VALUES (%s, %s, %s, %s, %s, %s);""",
            (str(b_id), pickup, drop, str(distance), curr_time.strftime("%H:%M:%S"), new_currtime.strftime("%H:%M:%S"))
        )
        self.db.commit()
    
    def get_trip(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW curr_trip AS SELECT * FROM trip;"""
        )
        cur.execute(
            """SELECT * FROM curr_trip;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW curr_trip;"""
        )
        return list(set(res))
    
    def get_current_ride(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW curr_rides AS SELECT * from booking WHERE booking.status='booked' and booking.driver_id=3;"""
        )
        cur.execute(
            """SELECT * FROM curr_rides;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW curr_rides;"""
        )
        return list(set(res))
    
    def get_past_bookings(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW past_books AS SELECT * from booking WHERE booking.driver_id=3;"""
        )
        cur.execute(
            """SELECT * FROM past_books;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW past_books;"""
        )
        return list(set(res))
    
    def get_past_trips(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW past_trips AS SELECT trip.booking_id, trip.pickuplocation, trip.droplocation, trip.distance, trip.starttime, trip.endtime from trip, booking WHERE booking.driver_id = 3 and trip.booking_id = booking.booking_id;;"""
        )
        cur.execute(
            """SELECT * FROM past_trips;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW past_trips;"""
        )
        return list(set(res))
    
    def your_vehicles(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW yourvehicles AS SELECT vehicles.vehicle_id, vehicles.currentlocation_id, vehicles.numberplate, vehicles.type, vehicles.fueltype, vehicles.brand, vehicles.model, vehicles.maxcapacity, vehicles.price, vehicles.interstatepermit, vehicles.rental, vehicles.availability, vehicles.dutystart, vehicles.dutyend from vehicles, drivers WHERE drivers.driver_id = 3 AND drivers.vehicle_id = vehicles.vehicle_id;"""
        )
        cur.execute(
            """SELECT * FROM yourvehicles;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW yourvehicles;"""
        )
        return list(set(res))
    
    def your_profile(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW profile AS SELECT * FROM drivers WHERE drivers.driver_id = 3;"""
        )
        cur.execute(
            """SELECT * FROM profile;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW profile;"""
        )
        return list(set(res))
    
    def insert_location(self, street, locality, city, state, pincode):
        cur = self.cursor
        cur.execute(
            """INSERT INTO location (street, locality, city, state, pincode) VALUES (%s, %s, %s, %s, %s);""",
            (street, locality, city, state, pincode)
        )
        self.db.commit()
    
    def insert_savedplaces(self):
        cur = self.cursor
        cur.execute(
            """SELECT * FROM location;"""
        )
        getrektlol = cur.fetchall()
        x = getrektlol[-1][0]
        cur.execute(
            """INSERT INTO savedplaces (customer_id, location_id) VALUES ('1', %s);""",
            (x,)
        )
        self.db.commit()
    
    def get_customer_users(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW cusers AS SELECT * FROM customer_users;"""
        )
        cur.execute(
            """SELECT * FROM cusers;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW cusers;"""
        )
        return list(set(res))
    
    def get_driver_users(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW dusers AS SELECT * FROM driver_users;"""
        )
        cur.execute(
            """SELECT * FROM dusers;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW dusers;"""
        )
        return list(set(res))
    
    def get_admin_users(self):
        cur = self.cursor
        cur.execute(
            """CREATE VIEW ausers AS SELECT * FROM admin_users;"""
        )
        cur.execute(
            """SELECT * FROM ausers;"""
        )
        res = cur.fetchall()
        cur.execute(
            """DROP VIEW ausers;"""
        )
        return list(set(res))