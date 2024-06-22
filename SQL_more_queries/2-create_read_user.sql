-- create a database and an user

CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
CREATE USER IN hbtn_0d_2 IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
