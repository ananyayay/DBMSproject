create table customer_users(
	email varchar(50),
    password varchar(20)
);

create table driver_users(
	email varchar(50),
    password varchar(20)
);

create table admin_users(
	email varchar(50),
    password varchar(20)
);




insert into customer_users values('customer1@coldmail.com','c111');
insert into customer_users values('customer2@coldmail.com','c222');
insert into customer_users values('customer3@coldmail.com','c333');

insert into driver_users values('driver1@coldmail.com','d111');
insert into driver_users values('driver2@coldmail.com','d222');
insert into driver_users values('driver3@coldmail.com','d333');

insert into admin_users values('admin1@coldmail.com','a111');
insert into admin_users values('admin2@coldmail.com','a222');
insert into admin_users values('admin3@coldmail.com','a333');

