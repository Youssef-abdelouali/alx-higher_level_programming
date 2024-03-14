-- This SQL command retrieves the count of records with the same score from the table named second_table on my MySQL server.
-- The counts are grouped by score and ordered in descending order based on the count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
