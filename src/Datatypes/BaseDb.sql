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
INSERT INTO teachers( initials, name ) VALUES('MON','Morten');
INSERT INTO teachers( initials, name ) VALUES('PFL','Poul');
INSERT INTO teachers( initials, name ) VALUES('PDA','Per');
INSERT INTO teachers( initials, name ) VALUES('PSS','Peder');
INSERT INTO teachers( initials, name ) VALUES('SUN','Susanne');
INSERT INTO teachers( initials, name ) VALUES('VL','Viggo');
INSERT INTO teachers( initials, name ) VALUES('HHAL','Helge');
INSERT INTO teachers( initials, name ) VALUES('BSZ','Bettina');
INSERT INTO teachers( initials, name ) VALUES('JLU','Jan');
INSERT INTO teachers( initials, name ) VALUES('IMR','Ib');
INSERT INTO teachers( initials, name ) VALUES('KESM','Kent');
INSERT INTO teachers( initials, name ) VALUES('SK','Stig');
INSERT INTO teachers( initials, name ) VALUES('HKR','Henrik');
INSERT INTO teachers( initials, name ) VALUES('NN','Endnu ukendt 1');
INSERT INTO teachers( initials, name ) VALUES('NN2','Endnu ukendt 2');



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

COMMIT;

