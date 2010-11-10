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


class GmailOutput_cli(GmailOutput):
    '''
    
    '''
    def __init__(self, username, password):
        '''
        Sets up user and passwd and connects to check that it works
        '''
        GmailOutput.__init(self, username, password)
    
        if not self.getListOfCalendars_cli().__contains__("owner"):
            raise IOError 
        
    def getListOfCalendars_cli(self):
        ''' Return a list of the calendars availible to the user '''
        return (Popen("gcalcli --user %s --pw %s --nc list"%( self._username, self._password), stdout=PIPE, shell=True).stdout.read()) 

    def addAppointment(self, Appointment):
        return self.addAppointment_cli(Appointment)

    def addAppointment_cli(self, Appointment):
        print ('gcalcli --user %s --pw %s --nc quick "%s"'%( self._username, self._password,self._appointmentToString_cli(Appointment)))
        #return (Popen('gcalcli --user %s --pw %s --nc quick "%s"'%( self._username, self._password,self._appointmentToString_cli(Appointment)), stdout=PIPE, shell=True).stdout.read()) 
              
    def _appointmentToString_cli(self, Appointment):
        appointmentString = ""
        appointmentString = appointmentString + Appointment.get("Hours")[0].strftime("%-d/%-m/%Y %H:%M") + "-" +Appointment.get("Hours")[1].strftime("%H:%M") + " "
        #appointmentString = appointmentString + Appointment.get("Hours")[0].strftime("%x %H:%M") + "-" +Appointment.get("Hours")[1].strftime("%H:%M") + " "
        appointmentString = appointmentString + Appointment.get("Subject") + " "
        appointmentString = appointmentString + Appointment.get("Location") + " "
        #appointmentString = appointmentString + Appointment.get("Class")
        return appointmentString
        
        
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
    
