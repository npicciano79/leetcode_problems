---1174 immedate food delivery
/*

Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
If the customer's preferred delivery date is the same as the order date,
 then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date
 that the customer made. It is guaranteed that a customer has precisely
  one first order.

Write an SQL query to find the percentage of immediate orders in the 
first orders of all customers, rounded to 2 decimal places.

*/



with cte AS(
  SELECT *
  FROM (
    SELECT customer_id,
    order_date,
    customer_pref_delivery_date,
    RANK() OVER( PARTITION BY customer_id ORDER BY order_date ASC) AS rk 
    FROM delivery
      ) AS temp
WHERE rk=1
),
cte_count AS(
  SELECT COUNT(*) AS order_count
  FROM cte
  WHERE cte.order_date=cte.customer_pref_delivery_date
)

SELECT ROUND(cte_count.order_count/COUNT(cte.customer_id)*100,2) AS immediate_percentage
FROM cte,cte_count;
