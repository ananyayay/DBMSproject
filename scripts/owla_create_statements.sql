CREATE TABLE `location` (
  `location_id` int unsigned NOT NULL AUTO_INCREMENT,
  `street` varchar(150) DEFAULT NULL,
  `locality` varchar(150) NOT NULL,
  `city` varchar(150) NOT NULL,
  `state` varchar(30) NOT NULL,
  `pincode` int unsigned NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `rentalpackages` (
  `package_id` int unsigned NOT NULL AUTO_INCREMENT,
  `vehicle_type` varchar(20) NOT NULL,
  `duration_hrs` int NOT NULL,
  `distance_km` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `trip` (
  `trip_id` int unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` int unsigned NOT NULL,
  `pickuplocation` int unsigned NOT NULL,
  `droplocation` int unsigned DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `starttime` time DEFAULT NULL,
  `endtime` time DEFAULT NULL,
  PRIMARY KEY (`trip_id`,`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `vehicles` (
  `vehicle_id` int unsigned NOT NULL AUTO_INCREMENT,
  `currentlocation_id` int unsigned NOT NULL,
  `numberplate` varchar(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  `fueltype` varchar(20) NOT NULL,
  `brand` varchar(30) DEFAULT NULL,
  `model` varchar(40) DEFAULT NULL,
  `maxcapacity` int NOT NULL,
  `price` int NOT NULL,
  `interstatepermit` tinyint(1) NOT NULL,
  `rental` tinyint(1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `dutystart` time NOT NULL,
  `dutyend` time NOT NULL,
  PRIMARY KEY (`vehicle_id`),
  KEY `currentlocation_id` (`currentlocation_id`),
  CONSTRAINT `vehicles_ibfk_1` FOREIGN KEY (`currentlocation_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `customers` (
  `customer_id` int unsigned NOT NULL AUTO_INCREMENT,
  `location_id` int unsigned DEFAULT NULL,
  `name` varchar(150) NOT NULL,
  `contact` mediumtext NOT NULL,
  `emailid` varchar(200) NOT NULL,
  `paymentmode` varchar(30) DEFAULT NULL,
  `savedplace1` int unsigned DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `drivers` (
  `driver_id` int unsigned NOT NULL AUTO_INCREMENT,
  `vehicle_id` int unsigned NOT NULL,
  `name` varchar(200) NOT NULL,
  `contact` mediumtext NOT NULL,
  `license` mediumtext NOT NULL,
  `rating` float NOT NULL,
  `tripscompleted` int NOT NULL,
  `noofratings` int NOT NULL,
  `earning` float NOT NULL,
  PRIMARY KEY (`driver_id`),
  KEY `vehicle_id` (`vehicle_id`),
  CONSTRAINT `drivers_ibfk_1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `olamoneyaccount` (
  `olamoneyaccount_id` int unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` int unsigned NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`olamoneyaccount_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `olamoneyaccount_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `payment` (
  `payment_id` int unsigned NOT NULL AUTO_INCREMENT,
  `trip_id` int unsigned NOT NULL,
  `booking_id` int unsigned NOT NULL,
  `customer_id` int unsigned NOT NULL,
  `modeofpayment` varchar(30) NOT NULL,
  `amount` float NOT NULL,
  `verdict` varchar(30) NOT NULL,
  PRIMARY KEY (`payment_id`,`trip_id`,`booking_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `savedplaces` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int unsigned NOT NULL,
  `location_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `savedplaces_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `savedplaces_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `search` (
  `search_id` int unsigned NOT NULL AUTO_INCREMENT,
  `booking_id` int unsigned DEFAULT NULL,
  `customer_id` int unsigned NOT NULL,
  `from_location` int unsigned NOT NULL,
  `to_location` int unsigned DEFAULT NULL,
  `vehicle_type` varchar(20) DEFAULT NULL,
  `ridetype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`search_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `search_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `shared` (
  `shared_id` int unsigned NOT NULL,
  `driver_id` int unsigned NOT NULL,
  PRIMARY KEY (`shared_id`),
  KEY `driver_id` (`driver_id`),
  CONSTRAINT `shared_ibfk_1` FOREIGN KEY (`driver_id`) REFERENCES `drivers` (`driver_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `booking` (
  `booking_id` int unsigned NOT NULL AUTO_INCREMENT,
  `driver_id` int unsigned NOT NULL,
  `customer_id` int unsigned NOT NULL,
  `from_location` int unsigned DEFAULT NULL,
  `to_location` int unsigned DEFAULT NULL,
  `timeofbooking` time NOT NULL,
  `scheduledtime` time DEFAULT NULL,
  `ridetype` varchar(20) NOT NULL,
  `noofpassengers` int NOT NULL,
  `isScheduled` tinyint(1) NOT NULL,
  `status` varchar(30) NOT NULL,
  `shared_id` int unsigned DEFAULT NULL,
  `package_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `driver_id` (`driver_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`driver_id`) REFERENCES `drivers` (`driver_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `bankaccount` (
  `account_id` int unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` int unsigned NOT NULL,
  `nameofholder` varchar(150) NOT NULL,
  `bank` varchar(150) NOT NULL,
  `branch` varchar(150) NOT NULL,
  `accountnumber` double NOT NULL,
  PRIMARY KEY (`account_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `bankaccount_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `cancelledrides` (
  `booking_id` int unsigned NOT NULL,
  `reason` varchar(300) DEFAULT NULL,
  `cancelledby` varchar(20) NOT NULL,
  `penalty` float NOT NULL,
  KEY `booking_id` (`booking_id`),
  CONSTRAINT `cancelledrides_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `transactions` (
  `transaction_id` int unsigned NOT NULL AUTO_INCREMENT,
  `olamoneyaccount_id` int unsigned NOT NULL,
  `account_id` int unsigned NOT NULL,
  `amount` float NOT NULL,
  `timeoftransaction` datetime NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `olamoneyaccount_id` (`olamoneyaccount_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`olamoneyaccount_id`) REFERENCES `olamoneyaccount` (`olamoneyaccount_id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`account_id`) REFERENCES `bankaccount` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `sharedbookings` (
  `shared_id` int unsigned NOT NULL,
  `booking_id` int unsigned NOT NULL,
  KEY `shared_id` (`shared_id`),
  KEY `booking_id` (`booking_id`),
  CONSTRAINT `sharedbookings_ibfk_1` FOREIGN KEY (`shared_id`) REFERENCES `shared` (`shared_id`),
  CONSTRAINT `sharedbookings_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE message (
    message_id int auto_increment,
    payment_id int unsigned,
    message varchar(300) not null,
    primary key (message_id),
    FOREIGN KEY(payment_id) REFERENCES
    payment(payment_id) ON DELETE SET NULL
);