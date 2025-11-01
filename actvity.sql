CREATE TABLE r (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);
INSERT INTO r (SNO , SNAME , STATUS , CITY ) VALUES
    ('S1', 'alpha', 999999999999, 'a'),
    ('S2', 'beta', 888888888, 'b'),
    ('S3', 'gamma', 7777777777777, 'c'),
    ('S4', 'delta', 123456789012345, 'd'),
    ('S5', 'epsilon', 42525424524250, 'e');
SELECT * FROM r;
