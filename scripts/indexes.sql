--INDEXES (INDICES) on drivers, vehicles, payment and savedplaces
--FOR admin queries

--Composite Index
CREATE INDEX idx_drivers_ratings
    on drivers (rating, noofratings);

--BTREE Index
CREATE INDEX idx_vehicle_type
    on vehicles(type);

--BTREE Index with ASC
CREATE INDEX idx_olamoneyaccount
    on payment( modeofpayment ASC );

--BTREE Index for COUNT
CREATE INDEX idx_savedplaces
    on savedplaces( location_id );
