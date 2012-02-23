#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 23 Feb 2012

@author: moz
'''

from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportSdeSkema import ImportSdeSkema
from Export.ExportFile import ExportFile
from Export.ExportIcs import ExportIcs
import os, filecmp, shutil
import sys

if __name__ == '__main__':
    # Read config/parameter
    config = SkemaPackConfig( open( sys.argv[1] ) )

    # Import from skema
    Events = ImportSdeSkema( config, "SkemaScraper" )

    # backup old fle
    outfile = config.get( "ExportFile", "OutFile")
    shutil.copy( outfile, outfile + u".old")

    # generate new file
    ExportFile( Events, config, "ExportFile" )
    
    # files differ
    if not filecmp.cmp( outfile, outfile + u".old" ):
        print "files differs. Dumping diff"
        os.system( "diff %s %s"%( outfile, outfile + u".old" ))

    # and output ics file
    ExportIcs( Events, config, "ExportIcs" )

    pass