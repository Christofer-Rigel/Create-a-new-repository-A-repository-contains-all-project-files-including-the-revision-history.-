CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INT PRIMARY KEY,
    FIRST_NAME TEXT,
    LAST_NAME TEXT,
    EMAIL TEXT UNIQUE,
    WHERE_FROM TEXT,
    GRADE INT
);
-- ATLEAST 20 NAMES MUST BE THERE ,AND AT LEAST 5 FROM NEW YORK , AND 4 WITH GRADE ABOVE 100
INSERT INTO CUSTOMERS (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, WHERE_FROM, GRADE) VALUES
(1, 'John', 'Doe', 'john.doe@example.com', 'USA', 5),
(2, 'Jane', 'Smith', 'jane.smith@example.com', 'Canada', 4),
(3, 'Alice', 'Johnson', 'alice.johnson@example.com', 'UK', 68),
(4, 'Bob', 'Brown', 'bob.brown@example.com', 'new york', 3),
(5, 'Charlie', 'Davis', 'charlie.davis@example.com', 'USA', 67),
(6, 'Eve', 'Miller', 'eve.miller@example.com', 'new york', 5),
(7, 'Frank', 'Wilson', 'frank.wilson@example.com', 'UK', 22),
(8, 'Grace', 'Moore', 'grace.moore@example.com', 'Australia', 43),
(9, 'Hank', 'Taylor', 'hank.taylor@example.com', 'new york', 5),
(10, 'Ivy', 'Anderson', 'ivy.anderson@example.com', 'Canada', 42),
(11, 'Jack', 'Thomas', 'jack.thomas@example.com', 'UK', 5),
(12, 'Kathy', 'Jackson', 'kathy.jackson@example.com', 'USA', 129),
(13, 'Leo', 'White', 'leo.white@example.com', 'Canada', 53),
(14, 'Mia', 'Harris', 'mia.harris@example.com', 'UK', 4),
(15, 'Nina', 'Martin', 'nina.martin@example.com', 'USA', 5);

SELECT *
FROM CUSTOMERS
WHERE WHERE_FROM NOT LIKE 'C%',
WHERE WHERE_FROM NOT LIKE 'A%',
WHERE WHERE_FROM NOT LIKE 'U%'
AND GRADE < 99;
