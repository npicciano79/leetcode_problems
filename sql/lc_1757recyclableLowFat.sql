#1757 recyclable and low fat products 

/*
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+

Write an SQL query to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
*/


SELECT product_id
FROM products
WHERE low_fats='Y' AND recyclable='Y';