CREATE TABLE IF NOT EXISTS Salesmen (
    Salesman-Id TEXT PRIMARY KEY,
    name TEXT,
    region TEXT,
    Commision TEXT,
    WHATtTHEYSELL TEXT
);
INSERT INTO Salesman(Salesman_id,name,city,Comision,WHATtTHEYSELL)
VALUES
    ("5001","james hong","New york","0.15","Sauces")    
    (,"5002","robert lee","Los angeles","0.12","Beverages")
    ("5003","maria garcia","Chicago","0.10","Snacks")
    ("5004","li wei","Houston","0.14","Dairy Products")
    ("5005","anna smith","Phoenix","0.11","Bakery Items")
    ("5006","john doe","Philadelphia","0.13","Frozen Foods")
    ("5007","sara kim","San antonio","0.16","Produce")
    ("5008","david brown","san diego","0.09","Meat Products")
    ("5009","linda johnson","dallas","0.08","Seafood")
    ("5010","james williams","san jose","0.07","Confectionery")
    ("5011","patricia taylor","austin","0.10","Canned Goods")
    ("5012","michael davis","jacksonville","0.12","Grains")
    ("5013","barbara moore","fort worth","0.11","Spices")
    ("5014","william thomas","columbus","0.13","Nuts")
    ("5015","elizabeth martin","charlotte","0.14","Oils and Vinegars")
    ("5016","jennifer jackson","san francisco","0.15","Breakfast Foods")
    ("5017","charles white","indianapolis","0.09","Deli Products")
    ("5018","mary harris","seattle","0.10","Health Foods")
    ("5019","joseph clark","denver","0.12","Baking Supplies")
    ("5020","susan lewis","washington","0.11","Ethnic Foods");
CREATE TABLE IF NOT EXISTS Customers (
    Customer-Id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT
);
INSERT INTO Customers(Customer_id,name,city,grade,Salesman_id)
VALUES
    ("3001","alice cooper","new york","A","5001"),
    ("3002","bob martin","los angeles","B","5002"),
    ("3003","carol white","chicago","A","5003"),
    ("3004","dave black","houston","C","5004"),
    ("3005","eve green","phoenix","B","5005"),
    ("3006","frank blue","philadelphia","A","5006"),
    ("3007","grace yellow","san antonio","C","5007"),
    ("3008","henry orange","san diego","B","5008"),
    ("3009","irene purple","dallas","A","5009"),
    ("3010","jack gray","san jose","C","5010"),
    ("3011","karen pink","austin","B","5011"),
    ("3012","leo cyan","jacksonville","A","5012"),
    ("3013","mia magenta","fort worth","C","5013"),
    ("3014","nick lime","columbus","B","5014"),
    ("3015","olivia teal","charlotte","A","5015"),
    ("3016","paul brown","san francisco","C","5016"),
    ("3017","quinn silver","indianapolis","B","5017"),
    ("3018","rachel gold","seattle","A","5018"),
    ("3019","sam bronze","denver","C","5019"),
    ("3020","tina copper","washington","B","5020");
CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);
INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,Salesman_id)
VALUES
    ("7001","1500","2023-01-15","3001","5001"),
    ("7002","2500","2023-02-20","3002","5002"),
    ("7003","1800","2023-03-10","3003","5003"),
    ("7004","2200","2023-04-05","3004","5004"),
    ("7005","3000","2023-05-12","3005","5005"),
    ("7006","2700","2023-06-18","3006","5006"),
    ("7007","3200","2023-07-22","3007","5007"),
    ("7008","2100","2023-08-30","3008","5008"),
    ("7009","1900","2023-09-14","3009","5009"),
    ("7010","2300","2023-10-03","3010","5010"),
    ("7011","2600","2023-11-11","3011","5011"),
    ("7012","2800","2023-12-19","3012","5012"),
    ("7013","2400","2024-01-25","3013","5013"),
    ("7014","2900","2024-02-28","3014","5014"),
    ("7015","3100","2024-03-15","3015","5015"),
    ("7016","2000","2024-04-20","3016","5016"),
    ("7017","1700","2024-05-27","3017","5017"),
    ("7018","3300","2024-06-08","3018","5018"),
    ("7019","3400","2024-06-18","3019","5019"),
    ("7020","3500","2024-06-25","3020","5020"); 1
-- Queries

--Matching customers and salesman by city
SELECT customer.cust_name, Salesman.name, salesman.city
FROM Customers customer
JOIN Salesmen salesman ON customer.city = salesman.region;
-- Fetching orders where customers city does not match salesman city
SELECT orders.ord_no, customer.name AS customer_name, salesman.name AS salesman_name
FROM Orders orders
JOIN Customers customer ON orders.customer_id = customer.Customer-Id
JOIN Salesmen salesman ON orders.Salesman_id = salesman.Salesman-Id
WHERE customer.city != salesman.region;
--fETCHING ALL ORDERS WITH CUSTOMER NAMES
SELECT Orders.ord_nom Customer.cust_name
FROM Orders
JOIN Customers Customer ON Orders.customer_id = Customer.Customer-Id;
-Customers with grades
SELECT Customer.cust_name AS "Customer", CUSTOMER.grade AS "Grade"
FROM Orders
JOIN Salesmen Salesman ON Orders.Salesman_id = Salesman.Salesman-Id
JOIN Customers Customer ON Orders.customer_id = Customer.Customer-Id;
--Customers with salesman commission where it is between 0.12 and 0.14
SELECT Orders.ORD_no, Customer.cust_name, Salesman.commission AS "Commission%",
Orders.punch_amt * Salesman.commision AS "Commission"
FROM Orders
JOIN Salesmen Salesman ON Orders.Salesman_id = Salesman.Salesman-Id
JOIN Customers Customer ON Orders.customer_id = Customer.Customer-Id
WHERE Salesman.commision BETWEEN 0.12 AND 0.14;
--orders on a specific date
SELECT *
FROM CUSTOMERS
JOIN Orders ON Customer.customer_id = Orders.customer_id
WHERE Orders.ord_date = '2012-05-12';