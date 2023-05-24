#180 consecutive numbers 

/*
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

Write an SQL query to find all numbers that appear at least three times consecutively.
Return the result table in any order.

*/

SELECT DISTINCT a.num AS ConsecutiveNums
FROM logs AS a, logs AS b, logs AS c 
WHERE a.num=b.num
AND b.num=c.num
AND b.id-1=a.id
AND c.id-1=b.id;