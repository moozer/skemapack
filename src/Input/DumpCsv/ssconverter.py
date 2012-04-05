#!/usr/bin/python
#
# Convert spreadsheet to CSV file.
#
# Based on:
#   PyODConverter (Python OpenDocument Converter) v1.0.0 - 2008-05-05
#   Copyright (C) 2008 Mirko Nasato <mirko@artofsolving.com>
#   Licensed under the GNU LGPL v2.1 - or any later version.
#   http://www.gnu.org/licenses/lgpl-2.1.html
#
# from:
#   http://www.linuxjournal.com/content/convert-spreadsheets-csv-files-python-and-pyuno
#
# MON:
#   Added filter options and a delimiter option
#   Added sheetname as parameter
#   Now issuing ValueError on bad Sheetname and IOError on bad filename

import os
import ooutils

import uno
from com.sun.star.task import ErrorCodeIOException
from com.sun.star.container import NoSuchElementException
from com.sun.star.lang import IllegalArgumentException

class SSConverter:
    """
    Spreadsheet converter class.
    Converts spreadsheets to CSV files.
    """

    def __init__(self, oorunner=None):
        self.desktop  = None
        self.oorunner = None


    def convert(self, inputFile, outputFile, SheetName = None, DelimiterInAscii = 9):
        """
        Convert the input file (a spreadsheet) to a CSV file.
        @param DelimiterInAscii: the delimiter. Default value \t (Ascii: 9) 
        """

        # Start openoffice if needed.
        if not self.desktop:
            if not self.oorunner:
                self.oorunner = ooutils.OORunner()

            self.desktop = self.oorunner.connect()

        inputUrl  = uno.systemPathToFileUrl(os.path.abspath(inputFile))
        outputUrl = uno.systemPathToFileUrl(os.path.abspath(outputFile))
        
        try:
            document  = self.desktop.loadComponentFromURL(inputUrl, "_blank", 0, ooutils.oo_properties(Hidden=True))
        except IllegalArgumentException, e:
            raise IOError( "Failed to open '%s': %s" % (inputFile, e.Message) )

        try:
            # Additional property option:
            #   FilterOptions="59,34,0,1"
            #     59 - Field separator (semicolon), this is the ascii value.
            #     34 - Text delimiter (double quote), this is the ascii value.
            #      0 - Character set (system).
            #      1 - First line number to export.
            #
            # For more information see:
            #   http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options
            #

            # change sheet is applicable
            if SheetName:
                sheet = document.Sheets.getByName(SheetName)
                
            document.storeToURL(outputUrl, ooutils.oo_properties(FilterName="Text - txt - csv (StarCalc)",
                                                                 FilterOptions="%d,34,76,1"%DelimiterInAscii))

        except NoSuchElementException:
            raise ValueError( "No sheet named '%s' in file '%s'"%(SheetName, inputFile))
        finally:
            document.close(True)


if __name__ == "__main__":
    from sys import argv
    from os.path import isfile

    if len(argv) == 2  and  argv[1] == '--shutdown':
        ooutils.oo_shutdown_if_running()
    else:
        if len(argv) < 3  or  len(argv) % 2 != 1:
            print "USAGE:"
            print "  python %s INPUT-FILE OUTPUT-FILE INPUT-FILE OUTPUT-FILE..." % argv[0]
            print "OR"
            print "  python %s --shutdown" % argv[0]
            exit(255)
        if not isfile(argv[1]):
            print "File not found: %s" % argv[1]
            exit(1)

        try:
            i = 1
            converter = SSConverter()

            while i+1 < len(argv):
                print '%s => %s' % (argv[i], argv[i+1])
                converter.convert(argv[i], argv[i+1])
                i += 2

        except ErrorCodeIOException, exception:
            print "ERROR! ErrorCodeIOException %d" % exception.ErrCode
            exit(1)