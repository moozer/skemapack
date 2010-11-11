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

from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile
from Output.IcsOutput.IcsOutput import IcsOutput

def ParseCmdLineOptions():
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-i", "--infile", dest="infile",
	                  help="File to read html data from", metavar="INFILE")
	parser.add_option("-u", "--url", dest="url", default="http://skema.sde.dk/laerer/5421/en-US.aspx",
	                  help="Skema url", metavar="URL")
	
	(options, args) =  parser.parse_args()
	
	#~ if options.infile and options.url:
		#~ parser.error( "-i and -u are mutually exclusive" )  
	
	return options


def main():
	opt = ParseCmdLineOptions()
	
	if opt.infile:
		try:
			Apps = ProcessFile( opt.infile )
		except IOError as e:
			print "Failed to open file %s. (Reason: %s)" % (opt.infile, e.strerror)
			return 0
	else:
		Apps = ProcessWebPage( opt.url)
	print len(Apps), "appointments extracted"
	
	#print Apps[0]['Subject']
	io = IcsOutput( Apps )

	FileName = "SkemaCurrentWeek.ics"
	f = open( FileName, "wb" )
	f.write( io.GetIcsString() )
	f.close()
	print "Ics file saved as", FileName
	
	return 0

if __name__ == '__main__': main()
