-- Displays the top 3 cities temperature during July and August
-- Results are ordered by average temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
