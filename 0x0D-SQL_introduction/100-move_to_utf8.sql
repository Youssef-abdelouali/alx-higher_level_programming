-- This SQL script converts the entire database named hbtn_0c_0 to the UTF-8 character encoding.
USE `hbtn_0c_0`;
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
