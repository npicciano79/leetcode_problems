---1479 sales by the day of the week
/*
Input: 
Orders table:
+------------+--------------+-------------+--------------+-------------+
| order_id   | customer_id  | order_date  | item_id      | quantity    |
+------------+--------------+-------------+--------------+-------------+
| 1          | 1            | 2020-06-01  | 1            | 10          |
| 2          | 1            | 2020-06-08  | 2            | 10          |
| 3          | 2            | 2020-06-02  | 1            | 5           |
| 4          | 3            | 2020-06-03  | 3            | 5           |
| 5          | 4            | 2020-06-04  | 4            | 1           |
| 6          | 4            | 2020-06-05  | 5            | 5           |
| 7          | 5            | 2020-06-05  | 1            | 10          |
| 8          | 5            | 2020-06-14  | 4            | 5           |
| 9          | 5            | 2020-06-21  | 3            | 5           |
+------------+--------------+-------------+--------------+-------------+
Items table:
+------------+----------------+---------------+
| item_id    | item_name      | item_category |
+------------+----------------+---------------+
| 1          | LC Alg. Book   | Book          |
| 2          | LC DB. Book    | Book          |
| 3          | LC SmarthPhone | Phone         |
| 4          | LC Phone 2020  | Phone         |
| 5          | LC SmartGlass  | Glasses       |
| 6          | LC T-Shirt XL  | T-Shirt       |
+------------+----------------+---------------+
Output: 
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Category   | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  | Sunday    |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Book       | 20        | 5         | 0         | 0         | 10        | 0         | 0         |
| Glasses    | 0         | 0         | 0         | 0         | 5         | 0         | 0         |
| Phone      | 0         | 0         | 5         | 1         | 0         | 0         | 10        |
| T-Shirt    | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

Write an SQL query to report how many units in each category have been ordered on each day of the week.

Return the result table ordered by category.


*/

SELECT i.item_category AS CATEGORY,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=0 THEN quantity ELSE 0 END)AS Monday,
     
        SUM(CASE WHEN WEEKDAY(o.order_date)=1 THEN quantity ELSE 0 END)AS Tuesday,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=2 THEN quantity ELSE 0 END)AS Wednesday,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=3 THEN quantity ELSE 0 END)AS Thursday,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=4 THEN quantity ELSE 0 END)AS Friday,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=5 THEN quantity ELSE 0 END)AS Saturday,
    
        SUM(CASE WHEN WEEKDAY(o.order_date)=6 THEN quantity ELSE 0 END)AS Sunday
FROM items as i LEFT JOIN orders AS o
ON i.item_id=o.item_id
GROUP BY i.item_category
ORDER BY i.item_category;