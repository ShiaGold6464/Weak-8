use whatabook ; 

drop table if exists wishlist ;
drop table if exists book ;
drop table if exists user ;
drop table if exists store ; 

create table store (
store_id  INT NOT NULL PRIMARY KEY,
locale VARCHAR(500) NOT NULL );

create table user ( 
user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
first_name VARCHAR (75) NOT NULL,
Last_name VARCHAR (75) NOT NULL );

create table book (
book_id  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
store_id INT NOT NULL  ,
book_name  VARCHAR (200) NOT NULL,
details   VARCHAR(500),
author  VARCHAR(200) NOT NULL ,
 FOREIGN KEY (store_id) references store (store_id)  );

Create table Wishlist (
wishlist_id  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
user_id   INT NOT NULL  ,
book_id  INT NOT NULL ,
FOREIGN KEY (user_id) references user (user_id),
FOREIGN KEY (book_id) references book (book_id)
); 

insert into store (store_id, locale)
values (1,"Newark");

select * from store ;

insert into book (book_id, store_id, book_name, details,  author)
values (1,1,"Steal like an artest","stealing theary","Harry");

insert into book (book_id, store_id, book_name, details,  author)
values (2,1,"Potter","magic powers","dale");

insert into book (book_id, store_id, book_name, details,  author)
values (3,1,"Life","How to live","Tom");

insert into book (book_id, store_id, book_name, details,  author)
values (4,1,"Erth","wiled life","josh pec");

insert into book (book_id, store_id, book_name, details,  author)
values (5,1,"Vale","A novel","ed");

insert into book (book_id, store_id, book_name, details,  author)
values (6,1,"The chef","How to cook like a pro","gordan");

insert into book (book_id, store_id, book_name, details,  author)
values (7,1,"sql in ten minutes","learn sql","tod");

insert into book (book_id, store_id, book_name, details,  author)
values (8,1,"Deth","the sad turth","huntter");

insert into book (book_id, store_id, book_name, details,  author)
values (9,1,"Moms","mom are great ","luky");


insert into user (user_id, first_name, last_name)
values (1,"jhon","doe");

insert into user (user_id, first_name, last_name)
values (2,"Potter","dale");

insert into user (user_id, first_name, last_name)
values (3,"Huntter","ven");



insert into wishlist (wishlist_id, user_id, book_id)
values (1, 2, 5);

insert into wishlist (wishlist_id, user_id, book_id)
values (2, 3, 4);

insert into wishlist (wishlist_id, user_id, book_id)
values (3, 1, 8);