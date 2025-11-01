CREATE TABLE COMPANY (
    EMPLOYEE_ID INT PRIMARY KEY,
    EMPLOYEE_NAME TEXT,
    DEPARTMENT TEXT,
    SALARY INT,
    CURRENT_JOB TEXT
);

INSERT INTO COMPANY (EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT, SALARY, CURRENT_JOB) VALUES
(1, 'Alice Johnson', 'Engineering', 90000, 'Software Engineer'),
(2, 'Bob Smith', 'Marketing', 75000, 'Marketing Manager'),
(3, 'Charlie Brown', 'Sales', 80000, 'Sales Executive'),
(4, 'Diana Prince', 'HR', 70000, 'HR Specialist'),
(5, 'Ethan Hunt', 'Engineering', 95000, 'DevOps Engineer'),
(6, 'Fiona Glenanne', 'Finance', 85000, 'Financial Analyst')
(7, 'George Costanza', 'Engineering', 72000, 'QA Engineer'),
(8, 'Hannah Montana', 'Marketing', 68000, 'Content Creator'),
(9, 'Ian Fleming', 'Sales', 78000, 'Account Manager'),
(10, 'Jane Doe', 'HR', 73000, 'Recruiter')
(11, 'Kevin Mitnick', 'Finance', 88000, 'Auditor');

SELECT * FROM COMPANY;