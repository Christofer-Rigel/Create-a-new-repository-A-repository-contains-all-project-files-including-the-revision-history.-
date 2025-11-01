CREATE TABLE IF NOT EXISTS DEPARTMENTS (
    EMPLOYEE_ID TEXT,
    NAME TEXT,
    DEPARTMENT_ID TEXT,
    MANAGER_ID TEXT,
    SALARY REAL
);

INSERT INTO DEPARTMENTS ( EMPLOYEE_ID, NAME, DEPARTMENT_ID , MANAGER_ID , SALARY ) VALUES
    ('E001', 'Alice Johnson', 'D001', 'M001', 75000),
    ('E002', 'Bob Smith', 'D002', 'M002', 62000),
    ('E003', 'Charlie Brown', 'D001', 'M001', 58000),
    ('E004', 'Diana Prince', 'D003', 'M003', 80000),
    ('E005', 'Ethan Hunt', 'D002', 'M002', 72000),
    ('E006', 'Fiona Glenanne', 'D003', 'M003', 69000),
    ('E007', 'George Costanza', 'D001', 'M001', 54000),
    ('E008', 'Hannah Montana', 'D002', 'M002', 66000),
    ('E009', 'Ian Fleming', 'D003', 'M003', 77000),
    ('E010', 'Jane Doe', 'D001', 'M001', 59000),
    ('E011', 'Kevin Mitnick', 'D002', 'M002', 64000),
    ('E012', 'Laura Croft', 'D003', 'M003', 81000),
    ('E013', 'Michael Scott', 'D001', 'M001', 56000),
    ('E014', 'Nina Williams', 'D002', 'M002', 68000),
    ('E015', 'Oscar Wilde', 'D003', 'M003', 73000),
    ('E016', 'Pam Beesly', 'D001', 'M001', 60000),
    ('E017', 'Quentin Tarantino', 'D002', 'M002', 65000),
    ('E018', 'Rachel Green', 'D003', 'M003', 78000),
    ('E019', 'Sam Winchester', 'D001', 'M001', 57000),
    ('E020', 'Tina Fey', 'D002', 'M002', 69000),
    ('E021', 'Uma Thurman', 'D003', 'M003', 82000),
    ('E022', 'Victor Hugo', 'D001', 'M001', 61000),
    ('E023', 'Wendy Darling', 'D002', 'M002', 63000),
    ('E024', 'Xander Cage', 'D003', 'M003', 76000),
    ('E025', 'Yvonne Strahovski', 'D001', 'M001', 58000),
    ('E026', 'Zoe Saldana', 'D002', 'M002', 67000);

SELECT DEPARTMENT_ID AS "Department Code",
COUNT(*) AS "No of employees"
FROM DEPARTMENTS
GROUP BY DEPARTMENT_ID;
SELECT DEPARTMENT_ID, SUM(SALARY)
FROM DEPARTMENTS
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "Department Code",
COUNT(*) AS "No of employees",
SUM(SALARY) AS "Total Salary"
FROM DEPARTMENTS
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "Department Code",
SUM(SALARY) AS "Total Salary"
FROM DEPARTMENTS
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "Department Code",
SUM(SALARY) AS "Total Salary"
FROM DEPARTMENTS
WHERE MANAGER_ID = 'E014';

SELECT DEPARTMENT_ID, COUNT(*) AS "No of employees"
FROM DEPARTMENTS
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) > 2;
