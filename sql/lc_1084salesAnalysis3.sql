#1084 sales analysis 3

/*
Product
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+

Sales
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |

Write an SQL query that reports the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
Return the result table in any order.
The query result format is in the following example

*/

SELECT DISTINCT p.product_id,p.product_name
FROM product as p
    LEFT JOIN sales AS s
    ON p.product_id=s.product_id
    GROUP BY p.product_id
HAVING min(s.sale_date)>='2019-01-01' AND max(s.sale_date)<='2019-03-31'