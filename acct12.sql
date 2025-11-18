CREATE TABLE IF NOT EXISTS nomnom (
    NAME TEXT,
    NEIGHBORHOOD TEXT,
    CUISINE TEXT,
    RATING TEXT,
    PRICE TEXT,
    REVIEW_COUNT TEXT,
    IS_HEALTHY TEXT,
    NO_DELIVERY INTEGER,
    NO_OF_DINING INTEGER
);

INSERT INTO nomnom(NAME, NEIGHBORHOOD, CUISINE, RATING, PRICE, REVIEW_COUNT, IS_HEALTHY, NO_DELIVERY, NO_OF_DINING)
VALUES  
    ("The Green Bowl","Downtown","Vegan","4.5","$$","150","Yes",0,50),
    ("Pasta Palace","Uptown","Italian","4.0","$$$","200","No",1,80),
    ("Sushi Central","Midtown","Japanese","4.8","$$$$","300","Yes",0,100),
    ("Burger Barn","Suburbs","American","3.5","$","120","No",1,30),
    ("Curry Corner","Downtown","Indian","4.2","$$","180","Yes",0,"60"),
    ("Taco Town","Uptown","Mexican","4.1","$","140","No",1,40),
    ("Healthy Bites","Midtown","Salads","4.7","$$$","220","Yes",0,70),
    ("Pizza Plaza","Suburbs","Italian","3.8","$$","160","No",1,90),
    ("Dim Sum Delight","Downtown","Chinese","4.6","$$$","250","Yes",0,110),
    ("BBQ Bliss","Uptown","Barbecue","4.3","$$$","190","No",1,55);
SELECT * FROM nomnom;

SELECT DISTINCT NEIGHBORHOOD FROM nomnom;

SELECT DISTINCT CUISINE FROM nomnom;

SELECT NAME, RATING, PRICE FROM nomnom WHERE CUISINE = "Italian";

SELECT * FROM nomnom WHERE PRICE = "$$" AND RATING >= "4.0";

SELECT NAME, CUISINE, RATING FROM nomnom WHERE IS_HEALTHY = "Yes" AND NO_DELIVERY = 0 ORDER BY RATING DESC;

SELECT NAME, CUISINE, PRICE FROM nomnom WHERE REVIEW_COUNT >= "200" ORDER BY PRICE ASC;

SELECT NAME, NEIGHBORHOOD, CUISINE, RATING FROM nomnom WHERE NEIGHBORHOOD = "Downtown" AND CUISINE = "Vegan";

SELECT NAME, CUISINE, RATING FROM nomnom WHERE NO_OF_DINING >= 50 ORDER BY RATING DESC;

SELECT * FROM nomnom WHERE CUISINE = "Japanese" OR CUISINE = "Chinese" AND PRICE = "$$$" ORDER BY RATING DESC;

SELECT * FROM nomnom WHERE NAME LIKE "%Bowl%" OR NAME LIKE "%Salads%";

SELECT * FROM nomnom
WHERE NEIGHBORHOOD IN ('midtown', 'Downtown','Chinatown')

SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;