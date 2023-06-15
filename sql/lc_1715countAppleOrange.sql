---1715 count apples and oranges
/*
Input: 
Boxes table:
+--------+----------+-------------+--------------+
| box_id | chest_id | apple_count | orange_count |
+--------+----------+-------------+--------------+
| 2      | null     | 6           | 15           |
| 18     | 14       | 4           | 15           |
| 19     | 3        | 8           | 4            |
| 12     | 2        | 19          | 20           |
| 20     | 6        | 12          | 9            |
| 8      | 6        | 9           | 9            |
| 3      | 14       | 16          | 7            |
+--------+----------+-------------+--------------+
Chests table:
+----------+-------------+--------------+
| chest_id | apple_count | orange_count |
+----------+-------------+--------------+
| 6        | 5           | 6            |
| 14       | 20          | 10           |
| 2        | 8           | 8            |
| 3        | 19          | 4            |
| 16       | 19          | 19           |
+----------+-------------+--------------+
Output: 
+-------------+--------------+
| apple_count | orange_count |
+-------------+--------------+
| 151         | 123          |
+-------------+--------------+

Write an SQL query to count the number of apples and oranges 
in all the boxes. If a box contains a chest, you should also include 
the number of apples and oranges it has.

*/

with apple_chest AS(
  SELECT chest_id, apple_count
  FROM chests
),
  orange_chest AS(
    SELECT chest_id, orange_count
    FROM chests
  )
SELECT(
  SELECT SUM(b.apple_count+IFNULL(ac.apple_count,0))
  FROM boxes AS b LEFT JOIN apple_chest AS ac
  ON b.chest_id=ac.chest_id
) AS apple_count,
(
  SELECT SUM(b.orange_count+IFNULL(oc.orange_count,0))
  FROM boxes AS b LEFT JOIN orange_chest AS oc
  ON b.chest_id=oc.chest_id
)AS orange_count