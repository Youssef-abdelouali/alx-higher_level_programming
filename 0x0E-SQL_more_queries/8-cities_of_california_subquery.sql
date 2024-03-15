-- List all cities of California in the hbtn_0d_usa database
-- List all rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
