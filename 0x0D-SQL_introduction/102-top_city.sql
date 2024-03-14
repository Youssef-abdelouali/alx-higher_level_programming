-- This SQL command retrieves the 3 cities with the highest average temperatures between July and August from the temperatures table in my MySQL server.
-- It filters the data for the months of July (month = 7) and August (month = 8), calculates the average temperature for each city, groups the results by city, orders them in descending order based on the average temperature, and limits the output to 3 rows.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
