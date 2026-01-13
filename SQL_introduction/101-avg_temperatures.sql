-- Displays the average temperature (Fahrenheit) by city
-- Results are ordered by average temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
