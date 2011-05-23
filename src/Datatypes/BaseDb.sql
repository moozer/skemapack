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

-- table containing all teachers to be used by the system.
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY, 
    initials TEXT, 
    name TEXT
    );
INSERT INTO teachers VALUES(1,'MON','Morten');
INSERT INTO teachers VALUES(2,'PFL','Poul');
INSERT INTO teachers VALUES(3,'PDA','Per');
INSERT INTO teachers VALUES(4,'PSS','Peder');
INSERT INTO teachers VALUES(5,'SUN','Susanne');
INSERT INTO teachers VALUES(6,'VL','Viggo');
INSERT INTO teachers VALUES(7,'HHAL','Helge');
INSERT INTO teachers VALUES(8,'BSZ','Bettina');
INSERT INTO teachers VALUES(9,'JLU','Jan');
INSERT INTO teachers VALUES(10,'IMR','Ib');
INSERT INTO teachers VALUES(11,'KESM','Kent');

COMMIT;

-- table containing class names
CREATE TABLE classes (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    alias_in_tf TEXT,
    official_denomination TEXT -- The offical name of the class in the schools systems.
    );
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("1. semester network", "1. Sem B Netværk", "asdf1234");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("2. semester network", "2. semester Network", "asdf1235");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("3. semester network", "3. Sem B Netværk", "asdf1236");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("3. semester network", "3.Networks", "asdf1236");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("4. semester network", "4. Communication", "asdf1237");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("1. semester electronics", "1. Sem A Elektronik", "asdf1234");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("2. semester electronics", "2. Sem Electronics", "asdf1235");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("3. semester electronics", "3. Electronics", "asdf1236");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("4. semester electronics", "4. Elektronik og Data", "asdf1237");
INSERT INTO classes( name, alias_in_tf, official_denomination) VALUES("4. semester electronics", "4. Networks", "asdf1237");

-- table containing semester definitions
CREATE TABLE semesters (
    id INTEGER PRIMARY KEY,
    long_name TEXT,
    Short_name TEXT,
    StartDate date,
    EndDate date                    
    );

-- activity table. 
-- the table with all activities like courses and vacation.
CREATE TABLE activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    alias_in_tf TEXT,
    teacher_id INTEGER,
    class_id INTEGER,
    semester_id INTEGER,
    prep_factor REAL,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
    FOREIGN KEY(class_id) REFERENCES classes(id)
    --FOREIGN KEY(semester_id) REFERENCES semesters(id)
    );

-- Lessons table
-- contains the list of which lessons per week
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_id INTEGER,
    week date, -- this is the date of the monday of the corresponding week
    number_of_lessons INTEGER,
    FOREIGN KEY (activity_id) REFERENCES activities( id )
);
