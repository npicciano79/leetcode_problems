---1398 customers who bought product A and B but not c
/*

Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+
Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
Output: 
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.
Return the result table ordered by customer_id.

*/

SELECT DISTINCT(c.customer_id),c.customer_name
FROM customers AS c LEFT JOIN orders AS o
ON c.customer_id=o.customer_id
WHERE c.customer_id NOT IN  (
  SELECT customer_id
  FROM orders 
  WHERE product_name='C'
)AND 
c.customer_id IN(
  SELECT customer_id
  FROM orders 
  WHERE product_name='A'
)AND 
c.customer_id IN(
  SELECT customer_id
  FROM orders
  WHERE product_name='B'
)
GROUP BY customer_id;