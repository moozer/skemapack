#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Extract list of URLs in a web page
"""

from BeautifulSoup import BeautifulSoup 
import urllib
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
import datetime
	
	
class SdeSkemaScraper( ):
	def __init__(self, DateFormat = "%m/%d/%Y", TimeFormat = "%H:%M", Teacher = ""):
		""" Initialisation """
		
		self.DateFormat = DateFormat
		self.TimeFormat = TimeFormat
		self.WeekdayDate = ""
		self.WeekDayCount = 0
		self.LessonCount = 0
		self.LessonContent = []
		self.LessonHours = []
		self.Appointments = []
		self.Teacher = Teacher
		
	def feed( self, data ):
		''' entry ser således ud
<div class="time">
<ul>
<li class="sHeader">Wednesday d.2/17/2010</li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">1</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">2 - 09:00 - 09:45</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain"><div class="sizer"><span class="sMainLektion">3 - 10:05 - 10:50</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">4 - 10:55 - 11:40</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain" ><div class="sizer"><span class="sMainLektion">5</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">6</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">7</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">8</span> <div class="sMainContent">&nbsp;</div></div></li>
</ul>
</div>
		'''
		self.soup = BeautifulSoup( data );
		for NewWeekDay in self.soup.findAll( 'div', {'class' : 'time'} ):
			if not self.IncWeekDay( str( NewWeekDay.find( 'li', {"class": "sHeader"} ).contents[0] ) ):
				continue;
			
			for NewLesson in NewWeekDay.findAll( 'div', {'class' : 'sizer'} ):
				# sprint NewLesson
				if not self.IncLesson( str( NewLesson.find( 'span', {"class": "sMainLektion"} ).contents[0] ) ):
					continue;
				
				for NewLessonContent in NewLesson.findAll( 'div', {'class' : 'sMainContent'} ):
					#if not self.IncLessonContent( NewLessonContent.contents ):
					#	print "skipped", NewLessonContent.contents
					#TODO: add support for meetings "Ingen Titel" in bold
					self.IncLessonContent( NewLessonContent.contents )

		# last lesson must be included also (provided it is not empty)
		if len( self.LessonContent ) > 0:
			self.DumpLesson()

			
	def IncWeekDay( self, data ):
		""" Function that is called when new weekday is detected"""
		if len( data ) <= 2:
			return False

		# TODOne: support more date formats. Particularly "04-10-2010"
		# already implemented by the constructor
		self.WeekdayDate = datetime.datetime.strptime( str.strip( data ).split("d.")[1], self.DateFormat )			
		self.WeekDayCount += 1
		self.LessonCount = 0
		#print "New weekday: ", self.WeekDayCount, " with title: ", self.WeekdayDate
		return True;
		
	def IncLesson( self, data ):
		""" 
		Function to be called when new lesson is encountered
		
		Saves the old lesson content and times as appointment, and starts to build the new one
		"""
		
		if len( data ) <= 2:
			return False
			
		if len( self.LessonContent ) > 0:
			self.DumpLesson()
		del self.LessonContent[:]
		self.LessonCount += 1
		
		# convert hours to absolute time using the current day as offset
		TmpSplit = str.split( data, " " )
		del self.LessonHours[:]
		for i in [2, 4]:
			TmpTime = datetime.datetime.strptime( TmpSplit[i], self.TimeFormat )
			TmpTimeSeconds = TmpTime.hour*60*60 + TmpTime.minute*60
			self.LessonHours.append( datetime.timedelta( 0, TmpTimeSeconds )+self.WeekdayDate )
			#print "lessonhours", self.LessonHours[-1]
		return True

		
	def IncLessonContent( self, data ):
		""" 
		Function to be called when lesson content is encountered
		
		Save data for later use
		"""
		
		# to avoid dummy entries
		if len( data ) <= 2:
			return False
		
		self.LessonContent = data
		return True
		
	def DumpLesson( self ):
		""" Appends current data as new appointment """
		# we use self.LessonHours[0].date() instead of self.WeekdayDate
		# because WeekDayDate is for the next entry.
		if len( self.LessonContent ) > 9:
			self.Appointments.append( {	"Date": self.LessonHours[0].date(), 
										"Hours": [self.LessonHours[0], self.LessonHours[1]], 
										"Subject": self.LessonContent[2].contents[0],
										"Class": self.LessonContent[6].contents[0],
										"Location": self.LessonContent[10].contents[0],
										"Teacher": self.Teacher
									} )
		else: # entries with "BOOKED"
			self.Appointments.append( {	"Date": self.LessonHours[0].date(), 
										"Hours": [self.LessonHours[0], self.LessonHours[1]], 
										#"Subject": unicode( self.LessonContent[2].contents[0], 'utf-8'),
										"Subject":  self.LessonContent[2].contents[0],
										"Class": "",
										"Location": "",
										"Teacher": self.Teacher
									} )
		#print "lesson dump", self.Appointments[-1]
	
	def close( self ):
		""" dummy function to be compatible"""
		return

def ProcessFile( FileToRead, DateFormat ):
	""" Utility function. Reads the files and pipes it to SkemaScraper 
	
	"""
	# TODO: The function should be moved elsewhere.
	f = open( FileToRead, "rb" )	
	data = f.read();
	parser = SdeSkemaScraper( DateFormat )
	parser.feed(data)
	parser.close()
	f.close()
	return  parser.Appointments 

def ProcessWebPageByUrl( UrlToOpen = "http://skema.sde.dk/laerer/5421/en-US.aspx", DateFormat = "%Y/%m/%d"  ):
	""" 
	Utility function. Fetches webpage from the internet and parses it
	
	@param UrlToOpen: The full url with the data to fetch, default "http://skema.sde.dk/laerer/5421/en-US.aspx" 
	@param DateFormat: The dateformat default %Y/%m/%d
	"""
	# TODO: The function should be moved elsewhere.
	usock = urllib.urlopen(UrlToOpen)
	parser = SdeSkemaScraper( DateFormat )
	parser.feed(usock.read())
	parser.close()
	usock.close()
	return  parser.Appointments 

def ProcessWebPageById( Id, FirstWeek, LastWeek, Year, DateFormat = "%Y/%m/%d"  ):
	""" 
	Utility function. Fetches webpage from the internet and parses it
	
	@param Id: The identifier of the teacher or room. @see: Input.HtmlGetter.LoadHtml.getSkemaWithPost
	@param FirstWeek: Start week of resulting schedule
	@param LastWweek: End week of resulting schedule	 
	@param Year: The year to extract data for. Defaults to current year.
	@param DateFormat: The dateformat. Defaults to "%Y/%m/%d"
	"""
	# TODO: The function should be moved elsewhere.
	myLoader = loadWeb.htmlGetter()
	parser = SdeSkemaScraper( DateFormat )
	parser.feed(myLoader.getSkemaWithPost(Id, FirstWeek, LastWeek, Year).read())
	parser.close()
	
	print myLoader.getParameters()
	return  parser.Appointments 
	
	
if __name__ == "__main__":
	app1 = ProcessWebPageByUrl( "http://skema.sde.dk/laerer/5421/en-US.aspx" )
	#for a in app1:
	#	print a["Date"], a["Hours"]

	print app1
	#app2 =ProcessWebPage( "http://skema.sde.dk/laerer/5421/da-DK.aspx" )
	#for a in app2:
	#	print a["Date"], a["Hours"]

