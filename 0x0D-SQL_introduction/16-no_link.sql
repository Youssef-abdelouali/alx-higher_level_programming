-- This SQL command retrieves all records from the table named second_table where the name value is not empty on my MySQL server.
-- The retrieved records are sorted in descending order based on the score attribute.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
