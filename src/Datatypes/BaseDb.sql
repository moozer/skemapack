BEGIN TRANSACTION;

PRAGMA foreign_keys = ON;

-- metadata table. some blabla mostly for later.
CREATE TABLE metadata (
    id INTEGER PRIMARY KEY, 
    key TEXT, 
    value TEXT
);
INSERT INTO metadata VALUES(1,'Skemapack version',0.1);
INSERT INTO metadata VALUES(2,'Generator','<none>');
INSERT INTO metadata VALUES(3,'Description','Basic db used for initialization');
INSERT INTO metadata VALUES(4,'Basedata origin','BaseDb.sqlite');
INSERT INTO metadata VALUES(5,'Title','No data');

-- table contaning all teachers to be used by the system.
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY, 
    initials TEXT, 
    name TEXT
    );
INSERT INTO teachers VALUES(1,'MON','Morten');
INSERT INTO teachers VALUES(2,'PFL','Poul');
COMMIT;

-- activity table. 
-- the table with all activities like courses and vacation.
CREATE TABLE activity (
    id INTEGER PRIMARY KEY,
    name TEXT,
    alias_in_tf TEXT,
    teacher_id INTEGER,
    class_id INTEGER,
    semester_id INTEGER,
    prep_factor REAL,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
    );

    