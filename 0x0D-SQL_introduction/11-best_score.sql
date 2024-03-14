-- This SQL command retrieves all records from the table named second_table where the score is greater than or equal to 10.
-- The retrieved records are sorted in descending order based on the score attribute.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
