---1107 New User Daily Count
/*
Traffic table:
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+
Output: 
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+

Write an SQL query to reports for every date within at most 90 
days from today, the number of users that logged in for the first 
time on that date. Assume today is 2019-06-30.


*/
with cte AS(
  SELECT t.user_id AS users,t.activity,MIN(t.activity_date) AS login_date
  FROM traffic AS t
  WHERE t.activity='login'
  GROUP BY t.user_id  
)
SELECT cte.login_date AS login_date,COUNT(cte.users) AS user_count
FROM cte
WHERE DATEDIFF('2019-06-30',login_date)<=90
GROUP BY login_date;