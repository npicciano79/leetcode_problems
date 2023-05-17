#1777 product price for each store
/*
Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
Output: 
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+

Write an SQL query to find the price of each product in each store.
*/

SELECT a.product_id,
  (SELECT DISTINCT price
  FROM products AS b
  WHERE store='store1' 
  AND a.product_id=b.product_id) AS store1,
  (SELECT DISTINCT price
  FROM products AS c
  WHERE store='store2' 
  AND a.product_id=c.product_id) AS store2,
  (SELECT DISTINCT price
  FROM products AS d
  WHERE store='store3' 
  AND a.product_id=d.product_id) AS store3
FROM Products AS a
GROUP BY product_id;
