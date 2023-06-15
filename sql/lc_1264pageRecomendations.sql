---1264 page recomendations
/*
Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
| 1        | 3        |
| 1        | 4        |
| 2        | 3        |
| 2        | 4        |
| 2        | 5        |
| 6        | 1        |
+----------+----------+
Likes table:
+---------+---------+
| user_id | page_id |
+---------+---------+
| 1       | 88      |
| 2       | 23      |
| 3       | 24      |
| 4       | 56      |
| 5       | 11      |
| 6       | 33      |
| 2       | 77      |
| 3       | 77      |
| 6       | 88      |
+---------+---------+
Output: 
+------------------+
| recommended_page |
+------------------+
| 23               |
| 24               |
| 56               |
| 33               |
| 77               |
+------------------+

Write an SQL query to recommend pages to the 
user with user_id = 1 using the pages that your friends 
liked. It should not recommend pages you already liked.


*/

#select all users friends with userid=1
SELECT DISTINCT l.page_id AS recommended_page
FROM LIKES AS l
WHERE l.user_id IN(
  SELECT f.user1_id
  FROM friendship AS f
  WHERE f.user2_id='1'
  UNION 
  SELECT f.user2_id
  FROM friendship AS f
  WHERE f.user1_id=1
)
AND l.page_id NOT IN (
  SELECT l.page_id
  FROM likes AS l
  WHERE l.user_id='1'
);