USE dict;
CREATE TABLE  user (
  name VARCHAR(32)  PRIMARY KEY  not null,
  passwd varchar(16) not null
);

CREATE TABLE history (
  word VARCHAR(64) NOT NULL ,
  time VARCHAR(128),
  name VARCHAR(32) NOT NULL
);

