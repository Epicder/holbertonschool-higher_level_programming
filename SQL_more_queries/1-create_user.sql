-- Create a user

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS;
GRANT * ON *.* TO 'user_0d_1'@'localhost';