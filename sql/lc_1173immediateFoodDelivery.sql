#1173 immediate food delivery
/*
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

*/

SELECT ROUND(SUM(order_date=customer_pref_delivery_date)/COUNT(*)*100,2) AS immediate_percentage
FROM delivery;