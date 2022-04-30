-- how many searches resulted in bookings
SELECT COUNT(*) as searches_that_resulted_in_bookings
    FROM search 
    WHERE booking_id IS NOT NULL;

-- display maximum saved location
SELECT street, locality, city, state, pincode 
    from location WHERE location_id = 
        (SELECT location_id AS most_saved_location
            FROM savedplaces 
            GROUP BY location_id 
            ORDER BY COUNT(*) 
            DESC LIMIT 1);

-- display top 10 rated drivers
SELECT * FROM drivers ORDER BY rating DESC LIMIT 10;

-- display top rated drivers with no of ratings > 80 
SELECT * FROM drivers WHERE noofratings>80 ORDER BY rating DESC LIMIT 10;

-- display drivers with 10 lowest earnings
SELECT * FROM drivers ORDER BY earning LIMIT 10;

-- display all customers sharing a ride with customer 25
SELECT customers.customer_id,name,contact,emailid
    FROM customers,booking
    WHERE customers.customer_id = booking.customer_id 
        and shared_id = 
            (SELECT shared_id 
                FROM booking 
                WHERE customer_id = 25);

-- Show all payments for trip_id 1
SELECT * FROM payment WHERE trip_id = 1;

-- display all drivers in the same location as the from vehicle current location and vehicle type in search id 101
SELECT driver_id, drivers.vehicle_id, name, contact, license
    FROM drivers, search, vehicles 
    WHERE search.search_id= 101 
        and drivers.vehicle_id = vehicles.vehicle_id 
        and search.from_location = vehicles.currentlocation_id 
        and search.vehicle_type = vehicles.type;

-- drivers with same location

-- if city ride:
SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
        and pickup = vehicles.currentlocation_id 
        and vehicles.type = cartype 
        and vehicle.availability=1;

-- if oustation:
SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
        and pickup = vehicles.currentlocation_id 
        and vehicles.type = cartype 
        and vehicle.availability=1 
        and interstatepermit=1;

-- if rental:
SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
        and pickup = vehicles.currentlocation_id 
        and vehicles.type = cartype 
        and vehicle.availability=1 
        and rental=1;

-- if shared:
SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
        and pickup = vehicles.currentlocation_id 
        and vehicles.type = cartype 
        and vehicle.availability=1 
        and maxcapacity>1;

-- SECOND TABLE:
SELECT drivers.name, drivers.contact, drivers.rating, drivers.tripscompleted, vehicles.numberplate, vehicles.brand, vehicles.model, vehicles.type, vehicles.fueltype 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
    and drivers.driver_id = id;

-- if when='now'
INSERT into booking (driver_id, customer_id, from_location, to_location, timeofbooking, scheduledtime, ridetype, noofpassengers, isScheduled, status) values d_id, 1, pickup, drop, time, NULL, ridetype, 1, 0, booked

-- if when!='now'
INSERT into booking (driver_id, customer_id, from_location, to_location, timeofbooking, scheduledtime, ridetype, noofpassengers, isScheduled, status) values d_id, 1, pickup, drop, time, when, ridetype, 1, 1, booked

-- show booking:
SELECT drivers.name, drivers.contact, from_location, to_location, timeofbooking, scheduledtime, ridetype, noofpassengers, status FROM drivers, booking WHERE drivers.driver_id = booking.driver_id AND customer_id='1' AND booking.status='booked';


-- find 3rd highest earning driver
SELECT driver_id, name, contact, earning from drivers d1 WHERE 2 = (SELECT COUNT(DISTINCT(d2.earning)) FROM drivers d2 WHERE d2.earning>d1.earning);

-- show the pickup locations and payment method customers used to pay for that trip.
SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;

-- fetch the vehicle type wise count of vehicles sorted by vehicle's count in descending order
SELECT type, COUNT(type) number_of_vehicles FROM vehicles GROUP BY type ORDER BY number_of_vehicles DESC;

-- display name contact emailid of all customers who have an ola money account id
SELECT customers.customer_id, name,contact,emailid FROM customers WHERE EXISTS (SELECT * FROM olamoneyaccount WHERE olamoneyaccount.customer_id = customers.customer_id);

-- drivers in the locations saved nearby 
SELECT driver_id, drivers.vehicle_id, name, contact, license 
    FROM drivers, search, vehicles 
    WHERE search.search_id= 101 
        and drivers.vehicle_id = vehicles.vehicle_id 
        and search.from_location = vehicles.currentlocation_id 
        and search.vehicle_type = vehicles.type;

-- saved location
CREATE VIEW saved_places_view as 
SELECT location FROM savedplaces WHERE customer_id= 1;

-- wallet
SELECT balance FROM olamoneyaccount WHERE customer_id= 1;
SELECT amount, timeoftransaction FROM transactions WHERE transactions.olamoneyd= 1;

-- RIDES HISTORY FOR CUSTOMER:

-- cancelled:
SELECT from_location, to_location, timeofbooking, ridetype, status, reason, cancelledby, penalty 
    from booking, cancelledrides 
    WHERE booking.customer_id=1 
        AND booking.status='cancelled' 
        AND cancelledrides.booking_id=booking.booking_id;

-- rentals:
SELECT from_location, to_location, timeofbooking, ridetype, status, vehicle_type, duration_hrs, distance_km from booking, rentalpackages WHERE booking.customer_id=1 AND rentalpackages.package_id=booking.package_id;

-- shared:
SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype="shared";

-- outstation:
SELECT from_location, to_location, timeofbooking, ridetype, status from booking WHERE booking.customer_id=1 AND booking.ridetype="outstation";

-- query for view using join
CREATE VIEW query10 AS SELECT booking.from_location, payment.modeofpayment, payment.verdict FROM booking LEFT JOIN payment ON booking.booking_id = payment.booking_id;

-- query for view named query6
CREATE VIEW query6 AS SELECT customers.customer_id,name,contact,emailid FROM customers,booking WHERE customers.customer_id = booking.customer_id and shared_id = (SELECT shared_id FROM booking WHERE customer_id = 25);

-- savedlocs
CREATE VIEW savedlocs AS 
    SELECT l.street, l.locality, l.city, l.state, l.pincode 
    FROM location AS l, 
        customers AS c, 
        savedplaces AS sp 
            WHERE sp.customer_id=1 
            AND sp.location_id=l.location_id;

-- view from most_saved_location
CREATE VIEW query2 AS 
    SELECT street, locality, city, state, pincode 
    from location 
    WHERE location_id = 
        (SELECT location_id AS most_saved_location 
            FROM savedplaces 
            GROUP BY location_id 
            ORDER BY COUNT(*) 
            DESC LIMIT 1);

-- driver details
CREATE VIEW query8 AS 
    SELECT driver_id, drivers.vehicle_id, name, contact, license
    FROM drivers, search, vehicles
    WHERE search.search_id= 101 
        and drivers.vehicle_id = vehicles.vehicle_id 
        and search.from_location = vehicles.currentlocation_id 
        and search.vehicle_type = vehicles.type;


-- query for near by driver
CREATE VIEW nearbydr AS 
    SELECT driver_id, drivers.vehicle_id, name, contact, license, brand, model, price 
    FROM drivers, vehicles 
    WHERE drivers.vehicle_id = vehicles.vehicle_id 
        and %s = vehicles.currentlocation_id 
        and vehicles.type = %s 
        and vehicles.availability=1 
        and interstatepermit=1;
    

-- query for your vehicles
CREATE VIEW yourvehicles AS 
    SELECT vehicles.vehicle_id, vehicles.currentlocation_id, vehicles.numberplate, vehicles.type, 
        vehicles.fueltype, vehicles.brand, vehicles.model, vehicles.maxcapacity, vehicles.price, 
        vehicles.interstatepermit, vehicles.rental, vehicles.availability, vehicles.dutystart, vehicles.dutyend 
    from vehicles, drivers 
    WHERE drivers.driver_id = 3 
        AND drivers.vehicle_id = vehicles.vehicle_id;