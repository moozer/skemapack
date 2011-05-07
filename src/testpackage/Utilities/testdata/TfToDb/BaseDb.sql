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
INSERT INTO teachers VALUES(1,'Teacher1','the first teacher entry');
INSERT INTO teachers VALUES(2,'Teacher2','the second teacher entry');
INSERT INTO teachers VALUES(3,'Teacher 3','the third teacher entry');
INSERT INTO teachers VALUES(4,'Teacher 5','the fourth teacher entry');
INSERT INTO teachers VALUES(5,'Teacher 6','the fifth teacher entry');
INSERT INTO teachers VALUES(6,'Teacher 7','the sixth teacher entry');
INSERT INTO teachers VALUES(7,'Teacher 8','the eighth teacher entry');
INSERT INTO teachers VALUES(8,'Teacher 9','bla');
INSERT INTO teachers VALUES(9,'Teacher 10','bla');
INSERT INTO teachers VALUES(10,'Teacher 11','bla');
INSERT INTO teachers VALUES(11,'Teacher 12','bla');
INSERT INTO teachers VALUES(12,'Teacher 13','bla');
COMMIT;

-- table containing class names
CREATE TABLE classes (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    alias_in_tf TEXT,
    official_denomination TEXT -- The offical name of the class in the schools systems.
    );
INSERT INTO classes VALUES(1, "1. semester network", "1. sem netværk", "asdf1234");
INSERT INTO classes VALUES(2, "2. semester network", "2. sem netværk", "asdf1235");
INSERT INTO classes VALUES(3, "3. semester network", "3. sem netværk", "asdf1236");
INSERT INTO classes VALUES(4, "4. semester network", "4. sem netværk", "asdf1237");
INSERT INTO classes VALUES(5, "1. Sem A Elektronik", "1. Sem A Elektronik", "asdf1236");
INSERT INTO classes VALUES(6, "1. Sem B Netværk", "1. Sem B Netværk", "asdf1236");
INSERT INTO classes VALUES(7, "3.Networks", "3.Networks", "asdf1236");
INSERT INTO classes VALUES(8, "3. Electronics", "3. Electronics", "asdf1236");
INSERT INTO classes VALUES(9, "4. Communication", "4. Communication", "asdf1236");



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
)    
