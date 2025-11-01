CREATE TABLE IF NOT EXISTS NOBEL_WIN (
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATAGORY TEXT
);

INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATAGORY) VALUES
    (1970, 'Physics', 'Hannes Alfven', 'Sweden', 'Nobel Prize in Physics'),
    (1971, 'Chemistry', 'Gerhard Herzberg', 'Canada', 'Nobel Prize in Chemistry'),
    (1972, 'Peace', 'Henry Kissinger', 'USA', 'Nobel Peace Prize'),
    (1973, 'Literature', 'Patrick White', 'Australia', 'Nobel Prize in Literature'),
    (1974, 'Medicine', 'Albert Claude', 'Belgium', 'Nobel Prize in Physiology or Medicine'),
    (1975, 'Economics', 'Leonid Kantorovich', 'USSR', 'Nobel Memorial Prize in Economic Sciences'),
    (1976, 'Physics', 'Burton Richter', 'USA', 'Nobel Prize in Physics'),
    (1977, 'Chemistry', 'Ilya Prigogine', 'Belgium', 'Nobel Prize in Chemistry'),
    (1978, 'Peace', 'Anwar Sadat', 'Egypt', 'Nobel Peace Prize'),
    (1979, 'Literature', 'Odysseas Elytis', 'Greece', 'Nobel Prize in Literature');

SELECT *
FROM NOBEL_WIN
WHERE SUBJECT NOT LIKE 'P%';                