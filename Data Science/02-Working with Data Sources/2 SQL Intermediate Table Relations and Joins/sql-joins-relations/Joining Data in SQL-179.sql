## 1. Introducing Joins ##

SELECT * from facts
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 10

## 2. Understanding Inner Joins ##

SELECT c.*, f.name country_name from facts f
INNER JOIN cities c ON c.facts_id = f.id
LIMIT 5

## 3. Practicing Inner Joins ##

SELECT f.name country, c.name capital_city from facts f
INNER JOIN cities c ON c.facts_id = f.id
WHERE c.capital = 1 

## 4. Left Joins ##

SELECT f.name country, f.population 
from facts f
LEFT JOIN cities c on c.facts_id = f.id
WHERE c.facts_id is NULL

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name capital_city, f.name country, c.population 
FROM facts f
INNER JOIN cities c ON c.facts_id = f.id
WHERE c.capital is 1
order By c.population DESC
LIMIT 10

## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city, f.name country, c.population 
FROM facts f
INNER JOIN (SELECT * from cities WHERE population > 10000000 AND capital = 1) c ON c.facts_id = f.id
order By c.population DESC

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT f.name country, c.urban_pop , f.population total_pop, (CAST(c.urban_pop as FLOAT) / CAST(f.population as FLOAT)) urban_pct
from facts f
INNER JOIN (SELECT facts_id, SUM(population) urban_pop from cities GROUP BY facts_id) c ON c.facts_id = f.id
WHERE urban_pct > 0.5 
ORDER BY urban_pct