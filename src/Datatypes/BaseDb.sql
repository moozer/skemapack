BEGIN TRANSACTION;
CREATE TABLE metadata (Id INTEGER PRIMARY KEY, Key TEXT, Value TEXT);
INSERT INTO metadata VALUES(1,'Skemapack version',0.1);
INSERT INTO metadata VALUES(2,'Generator','<none>');
INSERT INTO metadata VALUES(3,'Description','Basic db used for initialization');
INSERT INTO metadata VALUES(4,'Basedata origin','BaseDb.sqlite');
INSERT INTO metadata VALUES(5,'Title','No data');
COMMIT;
