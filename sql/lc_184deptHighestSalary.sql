--184 departmetn highest salary 
/*

Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

Write an SQL query to find employees who have the highest salary in each of the departments.
*/

SELECT d.name AS 'Department',
    e.name AS 'Employee',
    Salary

    FROM employee AS e LEFT JOIN department AS department
    ON e.departmentId=d.id
    WHERE 
        (e.departmentId,salary) IN 
        (
            SELECT e.departmentId,MAX(e.Salary)
            FROM Employee AS e  
            GROUP BY DepartmentId

        );