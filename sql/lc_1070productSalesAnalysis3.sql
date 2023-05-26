--1070 product sales analysis 3

/*
Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.
Return the resulting table in any order.

*/







SELECT p.product_id,s.year AS first_year,s.quantity,s.price
FROM sales AS s LEFT JOIN product AS p
ON p.product_id=s.product_id
WHERE (p.product_id,s.year)IN (
  SELECT product_id,MIN(year)
  FROM sales
  GROUP BY product_id
);