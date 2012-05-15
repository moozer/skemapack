#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       IcsOutput.py
#       
#       Copyright 2009  <morten@Epia>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

# import icalendar or die (with some help)
try:
	from icalendar import Event, Calendar
except: 
	print "Icalendar import error"
	print "Get the module from http://codespeak.net/icalendar/"
	exit()
	
class IcsOutput:
	def __init__( self, Appointments = [] ):
		""" constructor. Activates the parsing. """
		self.cal = Calendar()

		self.IcsHeader()
		self.AddAppointments( Appointments )

	def IcsHeader( self ):
		""" Add start stuff to the ICS file """
		self.cal.add('prodid', '-//My calendar product//mxm.dk//')
		self.cal.add('version', '2.0')
				
	def AddAppointments( self, Appointments ):
		""" adding appointments to ICS file (It is actually events) 
				event = Event()
event.add('summary', 'Python meeting about calendaring')


event.add('dtstart', datetime(2005,4,4,8,0,0,tzinfo=UTC))
  >>> event.add('dtend', datetime(2005,4,4,10,0,0,tzinfo=UTC))
event.add('dtstart', datetime(2005,4,4,8,0,0,tzinfo=UTC))

event.add('dtend', datetime(2005,4,4,10,0,0,tzinfo=UTC))
event.add('dtstamp', datetime(2005,4,4,0,10,0,tzinfo=UTC))
from icalendar import vCalAddress, vText
 organizer = vCalAddress('MAILTO:noone@example.com')
 organizer.params['cn'] = vText('Max Rasmussen')
organizer.params['role'] = vText('CHAIR')
event['organizer'] = organizer
event['location'] = vText('Odense, Denmark')
event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 5)
"""
		for App in Appointments:
			event = Event()
			if App.has_key( 'Class' ): 
				event.add('summary', App['Subject']+" - "+App['Class'])
			else:
				event.add('summary', App['Subject'])
			event.add('dtstart', App['Hours'][0])
			event.add('dtend', App['Hours'][1])
			
			if App.has_key( 'Location' ): event.add( 'location', App['Location'] )
			
			self.cal.add_component(event)
			# print "Event added", App
		
	def GetIcsString( self ):
		# iCalendar changed API (Im using the git master/HEAD 2012-5-13)
		# The output was also changed slightly -> knownResult file has been changed as well
		return self.cal.to_ical()

def main():
	from datetime import datetime
	SubjectName = unicode('System Design æøå', 'utf-8')
	apps = [{'Class': '09OIT3cH2', 'Date': datetime(2009, 11, 13, 0, 0), 'Hours': [datetime(2009, 11, 13, 12, 15), datetime(2009, 11, 13, 13, 0)], 'Location': 'A-301', 'Subject': SubjectName}]

	
	IO = IcsOutput( apps )
	print IO.GetIcsString(  )
	return 0

if __name__ == '__main__': main()
