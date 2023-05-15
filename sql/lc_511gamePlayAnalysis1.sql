#511 game play analysis 1

/*
Write an SQL query to report the first login date for each player.
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
*/

SELECT DISTINCT player_id,min(event_date) AS first_login
FROM Activity
GROUP BY player_id;