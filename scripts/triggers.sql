create table message (
	message_id int auto_increment,
    payment_id int,
    message varchar(300) not null,
    primary key (message_id),
    FOREIGN KEY(payment_id) REFERENCES payment(payment_id) ON DELETE SET NULL
);



Delimiter //
CREATE trigger check_ola_money 
	before INSERT ON payment 
		for each row 
		begin
			if new.modeofpayment = "Ola Money" and new.amount >
			    (select balance from olamoneyaccount where new.customer_id= olamoneyaccount.customer_id )
                    then set new.verdict= "Failed";

			else set new.verdict= "Success";	
        end if;
end //
Delimiter ;



Delimiter //
CREATE trigger notify_for_payment 
    after INSERT ON payment
    for each row 
        begin 
            if new.verdict= "Failed" and new.modeofpayment = "Ola Money" then
                insert into message 
                values (new.customer_id, new.payment_id, concat('Hi', new.customer_id, ', your olamoneyaccount balance is low. Kindly try another payment method'));

            else if new.verdict= "Success" then 
                insert into message 
                values (new.customer_id, new.payment_id, concat('Hi', new.customer_id, ', your payment received successfully'));

            end if;
        end if;
end //
delimiter ; 


Delimiter //
CREATE trigger add_driver_earnings 
	after INSERT ON payment 
		for each row 
		begin
			if new.verdict= "Success"
                then update drivers 
			    set drivers.earning= drivers.earning + new.amount
                where new.booking_id= booking.booking_id and booking.driver_id= drivers.driver_id; 
            end if;
end //
Delimiter ;

