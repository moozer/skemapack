'''
Created on Nov 9, 2010

@author: pfl
'''
from subprocess import Popen,PIPE



class GmailOutput():
    '''
    
    '''


    def __init__(self, username, password):
        '''
        Sets up user and passwd and connects to check that it works
        '''
        self._username = username
        self._password = password
    
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
        
        