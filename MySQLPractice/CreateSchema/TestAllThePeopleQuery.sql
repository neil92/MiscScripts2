/*
@Author: Neil A. Patel
Date: 2017-05-03

So I created the schema in:
SchemAllThePeopleCreation.sql

Here I fill it up and test it to make sure the
INNER JOIN works as expected.

*/



INSERT INTO person (name) VALUES ('Tom');
INSERT INTO person (name) VALUES ('Neil');

INSERT INTO tissue (location, person_id_fk) VALUES ('brain', 1);
INSERT INTO tissue (location, person_id_fk) VALUES ('liver', 2);
INSERT INTO tissue (location, person_id_fk) VALUES ('eyeball', 2);

SELECT * 
FROM person
JOIN tissue ON tissue.person_id_fk = person.person_id
WHERE person.`name` = 'Neil';
