#1873 calculate special bonus
/*
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
Output: 
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.

*/
SELECT employee_id,
  CASE
    WHEN employee_id IN (
      SELECT employee_id
      FROM employees
      WHERE employee_id%2!=0 
      AND LEFT(name,1)!='M'  
    )THEN salary
    ELSE 0
  END as bonus
  FROM employees
  ORDER BY employee_id ASC;