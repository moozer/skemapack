# -*- coding: UTF-8 -*-
'''
Created on Nov 15, 2010

    Classes for doing sumByDay and sumByWeek and a total of appointments

@author: pfl
'''

import datetime

class SumAppointments(object):
    '''
    used for summing up appointments. 
    sumByday returns array listing the load for each date.
    
    sumByDay()
    first element in the array is the start date as a datetime object, the second element is the list of load:
        [ "2010-10-22", [0,5,6,7,5,2,0,0,3,4,5,6,6,0,0]  ]
    
    sumByWeek()
    first element in the array is the first week number, the second element is a list of load per week:
        [ "43", [25,24] ]
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._appointments = []
        self._firstDate = datetime.date(2099,12,31)
        self._lastDate = datetime.date(1999,1,1)
        
    def addAppointment(self, Appointment):
        '''  add an appointment to the sum '''
        self._appointments.append(Appointment)
        
        if (self._firstDate > Appointment.get("Hours")[0].date()  ):
            self._firstDate = Appointment.get("Hours")[0].date()
        if (self._lastDate < Appointment.get("Hours")[0].date()  ):    
            self._lastDate = Appointment.get("Hours")[0].date()
        pass
    
    def sumByDay(self):
        sumByDay = []
        sumByWeek = []
        
        sum = [self._firstDate]
        return sum
    