/*
Write an SQL query to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
The query result format is in the following example.
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
*/


SELECT DISTINCT v.author_id AS ID
FROM Views AS v
WHERE v.author_id=v.viewer_id
ORDER BY v.author_id ASC;