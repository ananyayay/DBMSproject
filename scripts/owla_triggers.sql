Delimiter //

CREATE trigger check_ola_money 
  before INSERT ON payment 
    for each row begin

      if new.modeofpayment = "Ola Money" and new.amount >
        (select balance from olamoneyaccount
        
      where new.customer_id = olamoneyaccount.customer_id)
            
      then set new.verdict= "Failed";

      else set new.verdict= "Success";
   
      end if;
end //
Delimiter ;

Delimiter //
CREATE trigger notify_for_payment
	after INSERT ON payment
		for each row begin
			if new.verdict= "Failed" and new.modeofpayment = "Ola Money"
				then insert into message (message_id, message)
				values (new.customer_id, concat('Hi', new.customer_id, ', your
				olamoneyaccount balance is low. Kindly try another payment method'));
			else if new.verdict= "Success" then
				insert into message (message_id, message)
				values (new.customer_id, concat('Hi', new.customer_id, ', your payment
				received successfully'));
			end if;
			end if;
end //
delimiter ;

