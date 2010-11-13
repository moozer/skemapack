#!/usr/bin/env python
#
#       SkemaToIcs.py
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

from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPageById, ProcessWebPageByUrl, ProcessFile
from Output.IcsOutput.IcsOutput import IcsOutput
from optparse import OptionParser

def ParseCmdLineOptions():
	parser = OptionParser()
	parser.add_option("-i", "--infile", dest="infile",
	                  help="File to read html data from", metavar="INFILE")
	parser.add_option("-u", "--url", dest="url",
	                  help="Skema url", metavar="URL")
	parser.add_option("-d", "--date-format", dest="dateformat", default="%m/%d/%Y",
	                  help="Date format used", metavar="DATEFORMAT")	
	parser.add_option("-o", "--outfile", dest="outfile", default="SkemaCurrentWeek.ics",
	                  help="Filename of output file", metavar="OUTFILE")	
	parser.add_option("-I", "--Id", dest="id",
	                  help="Id of teacher or room", metavar="ID")	
	parser.add_option("-F", "--first-week", dest="FirstWeek", default="1",
	                  help="Start week of schedule", metavar="STARTWEEK")	
	parser.add_option("-E", "--end-week", dest="EndWeek", default="52",
	                  help="Lest week of schedule (included)", metavar="ENDWEEK")	
	
	(options, args) =  parser.parse_args()

	print options

	return options


def main():
	opt = ParseCmdLineOptions()

	try:
		if opt.infile:
			try: # processfile specific stuff
				Apps = ProcessFile( opt.infile, opt.dateformat )
			except IOError as e:
				print "Failed to open file %s. (Reason: %s)" % (opt.infile, e.strerror)
				exit( 1 )
		elif opt.url:
			Apps = ProcessWebPageByUrl( opt.url, opt.dateformat )
		elif opt.id:
			Apps = ProcessWebPageById( opt.id, opt.dateformat )
	except ValueError as e:
		print "Data reading or conversion failure. (Reason: %s)" % e.message
		print "If this is date conversion related consider using the --date-format option."
		exit( 2 )
	
	print len(Apps), "appointments extracted"
	
	#print Apps[0]['Subject']
	io = IcsOutput( Apps )

	f = open( opt.outfile, "wb" )
	f.write( io.GetIcsString() )
	f.close()
	print "Ics file saved as", opt.outfile
	
	return 0

if __name__ == '__main__': main()
