---574winning candidates
/*
Input: 
Candidate table:
+----+------+
| id | name |
+----+------+
| 1  | A    |
| 2  | B    |
| 3  | C    |
| 4  | D    |
| 5  | E    |
+----+------+
Vote table:
+----+-------------+
| id | candidateId |
+----+-------------+
| 1  | 2           |
| 2  | 4           |
| 3  | 3           |
| 4  | 2           |
| 5  | 5           |
+----+-------------+
Output: 
+------+
| name |
+------+
| B    |
+------+
Write an SQL query to report the name of the winning
 candidate (i.e., the candidate who got the largest 
 number of votes).

*/

with cte AS (
SELECT candidateId,COUNT(candidateId) AS val_occurance
  FROM vote
  GROUP BY candidateId
  ORDER BY val_occurance DESC
  LIMIT 1
)
SELECT c.name
FROM candidate AS c, cte
WHERE c.id=cte.candidateId;

