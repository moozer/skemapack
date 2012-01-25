# -*- coding: UTF-8 -*-
'''
Created on Nov 9, 2010

@author: pfl

http://code.google.com/apis/calendar/data/1.0/developers_guide_python.html#GettingStarted
'''
from subprocess import Popen,PIPE

try:
    import gdata.calendar.service
    import gdata.service
    import atom.service
    import gdata.calendar
    import atom
    import getopt
    import sys
    import string
    import time
except ImportError:
    print ("Google API import error.")
    # TODO: add link to gdata package

class GmailOutput():
    '''
    
    '''
    def __init__(self, username, password):
        '''
        Sets up user and passwd
        '''
        self._username = username
        self._password = password
        
        
class GmailOutput_API(GmailOutput):
    def __init__(self, username, password):
        GmailOutput.__init__(self, username, password)
        self.loginResult = self.connectToGoogle()
            
    def connectToGoogle(self):
        self.calendar_service = gdata.calendar.service.CalendarService()
        self.calendar_service.email = self._username
        self.calendar_service.password = self._password
        self.calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
        return self.calendar_service.ProgrammaticLogin()
            
    def addAppointment(self, Appointment):
        event = gdata.calendar.CalendarEventEntry()
        event.title = atom.Title(text= Appointment.get("Subject"))
        event.content = atom.Content(text= Appointment.get("Class"))
        event.where.append(gdata.calendar.Where(value_string= Appointment.get("Location")))
        event.when.append(gdata.calendar.When(start_time= Appointment.get("Hours")[0].strftime('%Y-%m-%dT%H:%M:%S.000'), end_time=Appointment.get("Hours")[1].strftime('%Y-%m-%dT%H:%M:%S.000') ))
        
        self.calendar_service.InsertEvent(event, '/calendar/feeds/default/private/full')
        pass
    
