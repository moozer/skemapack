'''
Created on May 5, 2011

@author: morten
'''

class ActivityData(object):
    '''
    Data container for course data.
    '''


    def __init__(self, Teacher, Class, Course, LessonsList ):
        '''
        Constructor
        '''
        self._Teacher = Teacher
        self._Class = Class
        self._Course = Course
        self._LessonsList = LessonsList
    
    # operators
    def __eq__(self, OtherCD ):
        ''' Equal operator. '''
        if( self._Teacher != OtherCD.getTeacher() ): return False
        if( self._Class != OtherCD.getClass() ): return False
        if( self._Course != OtherCD.getCourse() ): return False
        if( self._LessonsList != OtherCD.getLessonsList() ): return False
        return True

    # basic getters
    def getTeacher(self):
        return self._Teacher

    def setTeacher(self, Teacher):
        self._Teacher = Teacher

    def getClass(self):
        return self._Class
    
    def getCourse(self):
        return self._Course

    def getLessonsList(self):
        return self._LessonsList
    
    def getListOfWeeks(self):
        return self._LessonsList.keys()
    
    def getLessons(self, WeekNo):
        return self._LessonsList[WeekNo]
