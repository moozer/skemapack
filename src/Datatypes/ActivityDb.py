'''
Created on May 6, 2011

@author: morten
'''

import sqlite3
from Datatypes.ActivityData import ActivityData

class ActivityDb():
    '''
    classdocs
    '''

    def __init__(self, DbFile, BaseDbFile = u"Datatypes/BaseDb.sql"):
        '''
        Constructor
        @param DbFile The file to use. Try ':memory:'
        '''
        self._DbFile = DbFile
        self._conn = sqlite3.connect(DbFile)
        self._conn.row_factory = sqlite3.Row #we want to access rows by columnname

        self._BaseDbFile = BaseDbFile # sql file used for initialization of db

        # if db has emtadata, then it is accepted.
        try:
            self.GetMetadata()
        except sqlite3.OperationalError:
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

        c.execute( "select last_insert_rowid();" )
        ActivityId = c.fetchone()[0]

        Lessons = ActData.getLessonsList()
        for Week in Lessons.keys():
            values = (ActivityId, Lessons[Week], Week )
            c.execute( "insert into lessons (activity_id, number_of_lessons, week) values( ?,?,? ) ", values)
                    
        # Save (commit) the changes and close cursor
        self._conn.commit()
        c.close()
        
        return ActivityId
        
    def GetActivities(self, Teachers=[], Classes=[]):
        ''' returns an iterable object of ActivityData '''
        return self._ActivityList(self._conn, Teachers, Classes)
        
    def _ActivityList( self,conn, Teachers, Classes):
        ''' Makes the actual db call.
            functions as an iterator returning ActivityData objects '''
        c = conn.cursor()
        
        for query in self._MakeQuery(Teachers, Classes):
            c.execute(query)
        
            for row in c:
                LessonsList = self.GetLessonByActivityId( row['id'] )
                yield ActivityData( Teacher = row['teacher'], Class = row['class'], 
                                    Course = row['name'], LessonsList = LessonsList )
        
        raise StopIteration
    
    def _MakeQuery(self, Teachers, Classes):
        if Teachers!=[]: 
            for teacher in Teachers:
                queryActivities = '''
                    select     activities.id as id, activities.name as name, 
                               teachers.initials as teacher, classes.name as class 
                    from       activities, teachers, classes
                    '''
                queryActivities += "where      teachers.initials='%s'"%teacher
                queryActivities += '''
                    and        activities.teacher_id = teachers.id
                    and        activities.class_id = classes.id
                    '''
                yield queryActivities
        if Classes!=[]:
            for thisClass in Classes:
                queryActivities = '''
                    select     activities.id as id, activities.name as name, 
                               teachers.initials as teacher, classes.name as class 
                    from       activities, teachers, classes
                    '''
                queryActivities += "where      classes.name='%s'"%thisClass
                queryActivities += '''
                    and        activities.teacher_id = teachers.id
                    and        activities.class_id = classes.id
                    '''
                yield queryActivities
        if Teachers!=[] and Classes!=[]:
            queryActivities = '''
            select     activities.id as id, activities.name as name, 
                       teachers.initials as teacher, classes.name as class 
            from       activities, teachers, classes
            where      activities.teacher_id = teachers.id
            and        activities.class_id = classes.id
            '''
            yield queryActivities
        raise StopIteration

    def GetLessonByActivityId(self, ActId ):
        c = self._conn.cursor()
        queryLessons = 'select week, number_of_lessons from lessons where activity_id = ?'
        
        c.execute(queryLessons, (ActId,))

        LessonList = {}
        for row in c:
            LessonList[row['week']] = row['number_of_lessons']
        
        return LessonList
            
            