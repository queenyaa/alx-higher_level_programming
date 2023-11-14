-- Display the average temperature (F) by city ordered
-- by temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
