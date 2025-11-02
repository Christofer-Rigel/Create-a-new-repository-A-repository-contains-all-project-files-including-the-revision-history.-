CREATE TABLE CE (
    employee_id INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    minimum_salary INT,
    maximum_salary INT
);
INSERT INTO CE (employee_id, first_name, last_name, department, minimum_salary, maximum_salary) VALUES
(1, 'John', 'Doe', 'Engineering', 60000, 120000),
(2, 'Jane', 'Smith', 'Marketing', 50000, 100000),
(3, 'Emily', 'Johnson', 'Sales', 55000, 110000),
(4, 'Michael', 'Brown', 'HR', 45000, 90000),
(5, 'Jessica', 'Davis', 'Finance', 70000, 130000),
(6, 'Daniel', 'Miller', 'Engineering', 65000, 125000),
(7, 'Sarah', 'Wilson', 'Marketing', 52000, 102000),
(8, 'David', 'Moore', 'Sales', 58000, 115000),
(9, 'Laura', 'Taylor', 'HR', 47000, 95000),
(10, 'James', 'Anderson', 'Finance', 72000, 135000),
(11, 'Linda', 'Thomas', 'Engineering', 63000, 123000),
(12, 'Robert', 'Jackson', 'Marketing', 51000, 101000),
(13, 'Patricia', 'White', 'Sales', 56000, 112000),
(14, 'Charles', 'Harris', 'HR', 46000, 92000),
(15, 'Barbara', 'Martin', 'Finance', 71000, 132000),
(16, 'Steven', 'Thompson', 'Engineering', 64000, 124000),
(17, 'Elizabeth', 'Garcia', 'Marketing', 53000, 103000),
(18, 'Joseph', 'Martinez', 'Sales', 59000, 116000),
(19, 'Susan', 'Robinson', 'HR', 48000, 97000),
(20, 'Christopher', 'Clark', 'Finance', 73000, 136000),
(21, 'Karen', 'Rodriguez', 'Engineering', 66000, 126000),
(22, 'Matthew', 'Lewis', 'Marketing', 54000, 104000),
(23, 'Nancy', 'Lee', 'Sales', 60000, 117000),
(24, 'Anthony', 'Walker', 'HR', 49000, 98000),
(25, 'Margaret', 'Hall', 'Finance', 74000, 137000),
(26, 'Mark', 'Allen', 'Engineering', 67000, 127000),
(27, 'Sandra', 'Young', 'Marketing', 55000, 105000),
(28, 'Donald', 'Hernandez', 'Sales', 61000, 118000),
(29, 'Ashley', 'King', 'HR', 50000, 99000),
(30, 'Paul', 'Wright', 'Finance', 75000, 138000);

SELECT department AS "Department Code",
COUNT(*) AS "No of departments"
FROM department
GROUP BY department;
SELECT department, SUM(SALARY)
FROM department
GROUP BY department;

SELECT department AS "Department Code",
COUNT(*) AS "No of employees",
SUM(SALARY) AS "Total Salary"
FROM department
GROUP BY department;

SELECT department AS "Department Code",
SUM(SALARY) AS "Total Salary"
FROM department
GROUP BY department;

SELECT department AS "Department Code",
AVG(SALARY) AS "Average Salary"
FROM DEPARTMENTS
WHERE MANAGER_ID = 'E014';

