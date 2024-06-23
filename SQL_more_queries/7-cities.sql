-- create database and tables

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY (hbtn_0d_usa.states.id),
    name VARCHAR(256) NOT NULL
);