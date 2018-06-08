
set termout off

CREATE TABLE book
(
    title_id   CHAR(3)      NOT NULL,
    title_name VARCHAR(40)  NOT NULL,
    type       VARCHAR(10)  NULL    ,
    pub_id     CHAR(3)      NOT NULL,
    pages      INTEGER      NULL    ,
    price      DECIMAL(5,2) NULL    ,
    sales      INTEGER      NULL    ,
    pubdate    DATE         NULL    ,
    contract   SMALLINT     NOT NULL
);
INSERT INTO book VALUES('T01','Java','history','P01',111,21.99,566,DATE '2000-08-01',1);
INSERT INTO book VALUES('T02','Oracle','history','P03', 114,19.95,9566,DATE '1998-04-01',1);
INSERT INTO book VALUES('T03','SQL','computer','P02', 122,39.95,25667,DATE '2000-09-01',1);
INSERT INTO book VALUES('T04','C++','psychology','P04', 511,12.99,13001,DATE '1999-05-31',1);
INSERT INTO book VALUES('T05','Python','psychology','P04', 101,6.95,201440,DATE '2001-01-01',1);
INSERT INTO book VALUES('T06','JavaScript','biography','P01', 173,19.95,11320,DATE '2000-07-31',1);
INSERT INTO book VALUES('T07','LINQ','biography','P03', 331,23.95,1500200,DATE '1999-10-01',1);
INSERT INTO book VALUES('T08','C#','children','P04', 861,10.00,4095,DATE '2001-06-01',1);
INSERT INTO book VALUES('T09','SQL Server','children','P04', 212,13.95,5000,DATE '2002-05-31',1);
INSERT INTO book VALUES('T10','AJAX','biography','P01', NULL,NULL,NULL,NULL,0);
INSERT INTO book VALUES('T11','VB','psychology','P04', 821,7.99,94123,DATE '2000-11-30',1);
INSERT INTO book VALUES('T12','Office','biography','P01', 507,12.99,100001,DATE '2000-08-31',1);
INSERT INTO book VALUES('T13','VBA','history','P03', 812,29.99,10467,DATE '1999-05-31',1);

set termout on

SELECT title_id,
       price,
       0.10 AS "Discount",
       price * (1 - 0.10) AS "New price"
FROM book;

-- TIT      PRICE   Discount  New price
-- --- ---------- ---------- ----------
-- T01      21.99         .1     19.791
-- T02      19.95         .1     17.955
-- T03      39.95         .1     35.955
-- T04      12.99         .1     11.691
-- T05       6.95         .1      6.255
-- T06      19.95         .1     17.955
-- T07      23.95         .1     21.555
-- T08         10         .1          9
-- T09      13.95         .1     12.555
-- T10                    .1
-- T11       7.99         .1      7.191
--
-- TIT      PRICE   Discount  New price
-- --- ---------- ---------- ----------
-- T12      12.99         .1     11.691
-- T13      29.99         .1     26.991

drop table book;
