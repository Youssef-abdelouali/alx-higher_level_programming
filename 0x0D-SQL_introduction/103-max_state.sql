-- This SQL query retrieves the maximum temperature for each state from the temperatures table.
-- It calculates the maximum temperature for each state using the MAX function, aliasing it as 'max_temp'.
-- The results are grouped by state and ordered in ascending order based on the state name.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
