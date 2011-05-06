'''
Created on May 6, 2011

@author: morten
'''

import sqlite3, os

class ActivityDb():
    '''
    classdocs
    '''

    def __init__(self, DbFile):
        '''
        Constructor
        @param DbFile The file to use. Try ':memory:'
        '''
        self._DbFile = DbFile
        self._conn = sqlite3.connect(DbFile)

        self._BaseDbFile = "Datatypes/BaseDb.sql" # sql file used for initialization of db
        self._InitDb(self._BaseDbFile)
        
    def _InitDb( self, Filename ):
        ''' initializes database with data from sql file '''
        c = self._conn.cursor()

        # Create table
        f = open( Filename )
        sqldata = f.read()
        f.close()
        c.executescript(sqldata)
        
        # Save (commit) the changes and close cursor
        self._conn.commit()
        c.close()

    # ---- getters and setters ----------

    def GetMetadata(self):
        ''' returns the complete list of metadata '''
        c = self._conn.cursor()
        c.execute('select key, value from metadata')
        
        retval = {}
        for row in c:
            retval[row[0]] = row[1]

        return retval
   
    # --- Teacher table
    def GetTeacherList(self):
        ''' returns the complete list of metadata '''
        c = self._conn.cursor()
        c.execute('select initials, name from teachers')
        
        retval = {}
        for row in c:
            retval[row[0]] = row[1]

        return retval

    def GetTeacherId(self, TeacherIni ):
        ''' return the teacher id based on initials '''
        c = self._conn.cursor()
        c.execute("select id from teachers where initials=?", (TeacherIni,))
        
        try:
            return c.fetchone()[0]
        except TypeError:
            raise ValueError( "Teacher initials '%s' not found in database" % TeacherIni)

    # Class stuff
    def GetClassId(self, ClassName ):
        ''' return the teacher id based on initials '''
        c = self._conn.cursor()
        c.execute("select id from classes where name=? or alias_in_tf=?", (ClassName, ClassName))
        
        try:
            return c.fetchone()[0]
        except TypeError:
            raise ValueError( "Class name '%s' not found in database" % ClassName)

    # --------- insertions ------
    def AddActivity(self, ActData ):
        ''' adds an activity to table using ids from other tables. 
        @param ActData Data in the form of an ActivityData instance
        '''
        
        TeacherId = self.GetTeacherId( ActData.getTeacher() )
        ClassId = self.GetClassId( ActData.getClass() )

        c = self._conn.cursor()
        c.execute("insert into activities (name, teacher_id, class_id ) values (?,?,?)", 
                  (ActData.getCourse(), TeacherId, ClassId ))
        
        # Save (commit) the changes and close cursor
        self._conn.commit()
        c.close()
        
    def GetActivities(self):
        c = self._conn.cursor()
        c.execute("select * from activities")
        return c
        
        
        