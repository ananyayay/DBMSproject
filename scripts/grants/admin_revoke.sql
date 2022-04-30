--unused grants
grant all on owla.* to 'admin1@coldmail.com'@localhost;
grant all on owla.* to 'admin2@coldmail.com'@localhost;
grant all on owla.* to 'admin3@coldmail.com'@localhost;

-- revoke on tables
-- containing passwords of the users
revoke select on owla.admin_users from 'admin1@coldmail.com'@localhost;
revoke select on owla.customer_users from 'admin1@coldmail.com'@localhost;
revoke select on owla.driver_users from 'admin1@coldmail.com'@localhost;

revoke select on owla.admin_users from 'admin2@coldmail.com'@localhost;
revoke select on owla.customer_users from 'admin2@coldmail.com'@localhost;
revoke select on owla.driver_users from 'admin2@coldmail.com'@localhost;

revoke select on owla.admin_users from 'admin3@coldmail.com'@localhost;
revoke select on owla.customer_users from 'admin3@coldmail.com'@localhost;
revoke select on owla.driver_users from 'admin3@coldmail.com'@localhost;