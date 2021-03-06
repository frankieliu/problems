
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

create table book2 as (SELECT title_id, 1 as "tmp" FROM book);
alter table book2 add cumsum int;
select * from book2;

select book2.*,sum(book2(2)) over (order by book2.title_id) tot from book2;

set termout off
drop table book;
-- drop table book2;
set termout on
