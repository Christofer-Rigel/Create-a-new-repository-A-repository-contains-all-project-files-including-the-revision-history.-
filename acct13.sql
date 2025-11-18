CREATE TABLE IF NOT EXISTS employees (
    employee_name TEXT,
    department TEXT,
    salary TEXT,
    hire_date TEXT,
    boss_name TEXT
);
INSERT INTO employees(employee_name, department, salary, hire_date, boss_name)
VALUES
    ("Alice Johnson","Sales","60000","2020-03-15","Robert Smith"),
    ("Bob Williams","Marketing","55000","2019-07-22","Susan Davis"),
    ("Charlie Brown","IT","70000","2018-11-05","James Wilson"),
    ("Diana Prince","HR","52000","2021-01-30","Patricia Taylor"),
    ("Ethan Hunt","Finance","65000","2017-09-12","Michael Anderson"),
    ("Fiona Gallagher","Sales","62000","2020-06-18","Robert Smith"),
    ("George Martin","Marketing","58000","2019-04-25","Susan Davis"),
    ("Hannah Lee","IT","72000","2018-12-10","James Wilson"),
    ("Ian Somerhalder","HR","53000","2021-03-14","Patricia Taylor"),
    ("Jessica Alba","Finance","67000","2017-10-20","Michael Anderson");
-- Queries
-- Fetch all employees in the Sales department
SELECT * FROM employees WHERE department = "Sales"; 
-- Fetch employees with a salary greater than 60000
SELECT * FROM employees WHERE salary > "60000";
-- Fetch employees hired after January 1, 2019
SELECT * FROM employees WHERE hire_date > "2019-01-01";
-- Fetch employees whose boss is "Susan Davis"
SELECT * FROM employees WHERE boss_name = "Susan Davis";
-- Fetch employees in the IT department with a salary greater than 70000
SELECT * FROM employees WHERE department = "IT" AND salary > "70000";
-- Fetch employees hired before 2020 and in the Finance department
SELECT * FROM employees WHERE hire_date < "2020-01-01" AND department = "Finance";
-- Fetch employees whose names start with 'J'
SELECT * FROM employees WHERE employee_name LIKE "J%";
-- Fetch employees in Marketing or HR departments
SELECT * FROM employees WHERE department = "Marketing" OR department = "HR";
-- Fetch employees with salary between 55000 and 65000
SELECT * FROM employees WHERE salary BETWEEN "55000" AND "65000";
-- Fetch employees ordered by hire date descending
SELECT * FROM employees ORDER BY hire_date DESC;
-- Fetch top 3 highest paid employees
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;
-- Fetch employees whose department is either IT or Sales
SELECT * FROM employees WHERE department IN ('IT', 'Sales');
-- Fetch employees with salary not equal to 60000
SELECT * FROM employees WHERE salary != "60000";
-- Fetch employees hired in the year 2020
SELECT * FROM employees WHERE hire_date LIKE "2020%";
-- Fetch employees whose boss name contains 'Smith'
SELECT * FROM employees WHERE boss_name LIKE "%Smith%";