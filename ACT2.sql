CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commision REAL
);

INSERT INTO Salesman ( Salesman_id , name , city , commision ) VALUES
    ('9999', '𒀭ꙮẞᚠᛝ', 'Ⲉⲡⲓ⳨𑀓𑀸s', 99999999),
    ('6666', ': ᛣ҈Ӝཇ꧁⧉', '𐌔𐍂𐑃Ꮈⴲ', 66666),
    ('1234', '๏̵͇̿̿〠⇀', 'ᛗᚨᚾ𐰀𒌐', 4242),
    ('0001', '☭ᚹ𓂀𑁍઴', '⧉҉ƸӜƷ𒀱', 1),
    ('7777', '⊹꩜𖤐ⵔϞ', '𐰧𐰺𐰤ⳑ⚚', 12345689),
    ('8888', '⸸ⴲ҉𖣐𓂺꧞̷̸̵͟͞͠⛧͢͢͢͢҉҉𒐫𑁍𐰂𒀭̶̴̶⟟𑀓𖤍҈᷿᷾۞ꙮ𖤐⿻𑀧𑀤𖣘⧞⧽✺𒉽⳨𒂷', '𓁹𓆣Ⳃ⟟⧂⳯⸸𐰺꧅𑀸𖤍҉҉҉𑁍𓃾𐍂𒌐⳰☠︎𒀭⛧𖣐⚚𐰤𖣘꩜ⵔ𓂀҈҈҈𑀤⳨𖤐⿻∞𒉽𑁍', 314159265);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders {
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders (ord_no , purch_amt , ord_date,customer_id , Salesman_id) VALUES
    ('70001',158.5,'2012-10-05','3005','5002'),
    ('70009',2198.546,'2012-09-10','3001','5083'),
    ('70002',2342.234,'1393-98-18','3125','1231'),
    ('38678',731.3254,'1231-29-12','3987','1111'),
    ('70007', 82387.12321,'1-1-1','1234','1232'),

SELECT * FROM Orders;

SELECT name, commision
FROM salesman;