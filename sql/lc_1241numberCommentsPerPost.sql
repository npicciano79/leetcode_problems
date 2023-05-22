--1241 NUmber of comments per post
/*
+---------+------------+
| sub_id  | parent_id  |
+---------+------------+
| 1       | Null       |
| 2       | Null       |
| 1       | Null       |
| 12      | Null       |
| 3       | 1          |
| 5       | 2          |
| 3       | 1          |
| 4       | 1          |
| 9       | 1          |
| 10      | 2          |
| 6       | 7          |
+---------+------------+
Output: 
+---------+--------------------+
| post_id | number_of_comments |
+---------+--------------------+
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |

Write an SQL query to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.
The Submissions table may contain duplicate comments. You should count the number of unique comments per post.
The Submissions table may contain duplicate posts. You should treat them as one post.
The result table should be ordered by post_id in ascending order.
The query result format is in the following example.
*/

SELECT DISTINCT sub_id AS post_id,
(
    SELECT COUNT(DISTINCT sub_id)
    FROM submissions AS a2
    WHERE a1.sub_id=a2.parent_id
)AS number_of_comments 
FROM submissions AS a1
WHERE parent_id IS NULL 
GROUP BY sub_id
ORDER BY sub_id;