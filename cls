

create table words(
id int primary key auto_increment,
word varchar(20) not null,
mean varchar(1024) not null,
index (word)
);