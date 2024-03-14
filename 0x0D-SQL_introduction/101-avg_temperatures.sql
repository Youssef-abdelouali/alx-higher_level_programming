-- This SQL query calculates the average temperature (in Fahrenheit) for each city.
-- It selects the city and computes the average temperature, aliasing it as 'avg_temp'.
-- The results are grouped by city.
-- Finally, the results are ordered in descending order based on the average temperature.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
