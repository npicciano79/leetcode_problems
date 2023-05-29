--1468 calculate salaries 
/*
Salaries table:
+------------+-------------+---------------+--------+
| company_id | employee_id | employee_name | salary |
+------------+-------------+---------------+--------+
| 1          | 1           | Tony          | 2000   |
| 1          | 2           | Pronub        | 21300  |
| 1          | 3           | Tyrrox        | 10800  |
| 2          | 1           | Pam           | 300    |
| 2          | 7           | Bassem        | 450    |
| 2          | 9           | Hermione      | 700    |
| 3          | 7           | Bocaben       | 100    |
| 3          | 2           | Ognjen        | 2200   |
| 3          | 13          | Nyancat       | 3300   |
| 3          | 15          | Morninngcat   | 7777   |
+------------+-------------+---------------+--------+
Output: 
+------------+-------------+---------------+--------+
| company_id | employee_id | employee_name | salary |
+------------+-------------+---------------+--------+
| 1          | 1           | Tony          | 1020   |
| 1          | 2           | Pronub        | 10863  |
| 1          | 3           | Tyrrox        | 5508   |
| 2          | 1           | Pam           | 300    |
| 2          | 7           | Bassem        | 450    |
| 2          | 9           | Hermione      | 700    |
| 3          | 7           | Bocaben       | 76     |
| 3          | 2           | Ognjen        | 1672   |
| 3          | 13          | Nyancat       | 2508   |
| 3          | 15          | Morninngcat   | 5911   |
+------------+-------------+---------------+--------+

Write an SQL query to find the salaries of the employees after applying taxes. Round the salary to the nearest integer.
The tax rate is calculated for each company based on the following criteria:
0% If the max salary of any employee in the company is less than $1000.
24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
49% If the max salary of any employee in the company is greater than $10000.

*/

SELECT company_id, employee_id,employee_name,
    ROUND(
        CASE
        WHEN MAX(salary) OVER(PARTITION BY company_id)<1000 THEN salary
        WHEN MAX(salary) OVER(PARTITION BY company_id) >= 1000 AND MAX(salary) OVER(PARTITION  
        BY company_id)<=10000 THEN salary*0.76
        ELSE salary*0.51
        END
    )AS salary

FROM salaries;