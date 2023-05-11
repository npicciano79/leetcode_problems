--595 big countries
/*
---Write an SQL query to report the names, pop and area of countries 
---with an area >=3000000 or pop >=2500000

*/

SELECT name,area,population 
FROM World
WHERE population >=25000000 OR area>=3000000;