-- Create database hbtn_0d_usa and table states in hbtn_0d_usa database on MySQL server
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
