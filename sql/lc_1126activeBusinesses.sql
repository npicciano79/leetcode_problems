---1126 active Business
/*


The average activity for a particular event_type is the average
 occurences across all companies that have this event.
An active business is a business that has more than one 
event_type such that their occurences is strictly greater than 
the average activity for that event.
Write an SQL query to find all active businesses.

Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+
Output: 
+-------------+
| business_id |
+-------------+
*/

WITH cte AS(
  SELECT event_type, AVG(occurences) as averages 
  FROM events
  GROUP BY event_type
)
SELECT business_id
FROM events as e LEFT JOIN cte as c
ON e.event_type=c.event_type
WHERE e.occurences>c.averages
GROUP BY business_id
HAVING COUNT(business_id)>1;
