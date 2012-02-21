#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Sep 13, 2011

@author: morten
'''
from Other.PythonPathUtil import AppendSrcToPythonPath #@UnusedImport
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys
from Export.ExportFile import ExportFile

def ImportSdeSkema( config, ConfigSet = "SkemaScraper" ):
    ''' Config parameters: TeacherId, FirstWeek, LastWeek, Year, InputDateformat, 
            Infile (if set, read from file)
    '''
    # read data from file or net
    if config.has_option(ConfigSet, "Infile"):
        Data = open(config.get(ConfigSet, "Infile")).read()
    else:
        myLoader = loadWeb.htmlGetter()
        Data = myLoader.getSkemaWithPost(config.get(ConfigSet, "TeacherId"), 
                                     config.get(ConfigSet, "FirstWeek"), 
                                     config.get(ConfigSet, "LastWeek"), 
                                     config.get(ConfigSet, "Year")).read()
                                     
    # and process data
    parser = SdeSkemaScraper( config.get(ConfigSet, "InputDateformat"),
                              Teacher = config.get(ConfigSet, "Teacher" ) )
    parser.feed( Data )
    parser.close()
    
    # TODO: Decide on name for this, Appointments or Events
    return  parser.Appointments 


if __name__ == '__main__':

    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
    else:
        cfgfile = SkemaPackConfig_stdin()

#    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "SkemaScraper"

    # 3) import from skema
    Events = ImportSdeSkema( config, ConfigSet )
    
    # 4) output all events to stdout
    ExportFile( Events, config, ConfigSet )
    