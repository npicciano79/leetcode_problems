---1613 find missing ids
/*
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
Output: 
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+

Write an SQL query to find the missing customer IDs. The missing
 IDs are ones that are not in the Customers table but are in the range 
 between 1 and the maximum customer_id present in the table.
with RECURSIVE cte AS(
    SELECT 1 AS first_val
    UNION ALL
    SELECT first_val+1
    FROM cte
    WHERE first_val<(SELECT MAX(customer_id) FROM customers)
)

SELECT DISTINCT(first_val) as ids
FROM cte
WHERE first_val NOT IN (
  SELECT customer_id
  FROM customers
)
ORDER BY ids;

*/

