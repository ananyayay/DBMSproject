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
            """SELECT * FROM drivers ORDER BY rating DESC LIMIT 10;"""
        )
        res = cur.fetchall()
        return res
    
    def query_4(self):
        cur = self.cursor
        cur.execute(
            """SELECT * FROM drivers WHERE noofratings>80 ORDER BY rating DESC LIMIT 10;"""
        )
        res = cur.fetchall()
        return res
    
    def query_5(self):
        cur = self.cursor
        cur.execute(
            """SELECT * FROM drivers ORDER BY earning LIMIT 10;"""
        )
        res = cur.fetchall()
        return res
    
    def query_6(self):
        cur = self.cursor
        cur.execute(
            """SELECT customers.customer_id,name,contact,emailid FROM customers,booking WHERE customers.customer_id = booking.customer_id and shared_id = (SELECT shared_id FROM booking WHERE customer_id = 25);"""
        )
        res = cur.fetchall()
        return res
    
    def query_7(self):
        cur = self.cursor
        cur.execute(
            """SELECT * FROM payment WHERE trip_id = 1;"""
        )
        res = cur.fetchall()
        return res
    
    def query_8(self):
        cur = self.cursor
        cur.execute(
            """SELECT driver_id, drivers.vehicle_id, name, contact, license FROM drivers, search, vehicles WHERE search.search_id= 101 and drivers.vehicle_id = vehicles.vehicle_id and search.from_location = vehicles.currentlocation_id and search.vehicle_type = vehicles.type;"""
        )
        res = cur.fetchall()
        return res
    
    def query_9(self):
        cur = self.cursor
        cur.execute(
            """SELECT driver_id, name, contact, earning from drivers d1 WHERE 2 = (SELECT COUNT(DISTINCT(d2.earning)) FROM drivers d2 WHERE d2.earning>d1.earning);"""
        )
        res = cur.fetchall()
        return res
    
    def query_10(self):
        cur = self.cursor
        cur.execute(
            """SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;"""
        )
        res = cur.fetchall()
        return res
    
    def query_11(self):
        cur = self.cursor
        cur.execute(
            """SELECT type, COUNT(type) number_of_vehicles FROM vehicles GROUP BY type ORDER BY number_of_vehicles DESC;"""
        )
        res = cur.fetchall()
        return res
    
    def query_12(self):
        cur = self.cursor
        cur.execute(
            """SELECT customers.customer_id, name,contact,emailid FROM customers WHERE EXISTS (SELECT * FROM olamoneyaccount WHERE olamoneyaccount.customer_id = customers.customer_id);"""
        )
        res = cur.fetchall()
        return res