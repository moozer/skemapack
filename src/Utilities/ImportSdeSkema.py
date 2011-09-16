'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Configuration.SkemaPackConfig import SkemaPackConfig
from optparse import OptionParser
import os
import sys



def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-c", "--configfile", dest="ConfigFileName",
                      help="Load configuration from this file")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options



# TODOne: move to file that contains general import/export supprt functions

# TODO: move to support file
# TODO: Events should be a data type with event.__str__()
def PrintEvents( events ):
    for event in events:
        for key in event.keys():
            print "%s: %s; "%(key, event[key]),
        print "" # adding final newline
    
def ImportSdeSkema( config ):
    myLoader = loadWeb.htmlGetter()
    Data = myLoader.getSkemaWithPost(config.get("SkemaScraper", "TeacherId"), config.get("SkemaScraper", "FirstWeek"), config.get("SkemaScraper", "LastWeek"), config.get("SkemaScraper", "Year")).read()
    parser = SdeSkemaScraper( config.get("SkemaScraper", "Dateformat") )
    parser.feed( Data )
    parser.close()
    
    # TODO: Decide on name for this, Appointments or Events
    return  parser.Appointments 


if __name__ == '__main__':

    opt = ParseCmdLineOptions()
    print "commandLine options:"
    print opt
    
    
#    # 1) read config/parameter
    
    #TODO: this filename should not be hardcoded :)
    try:
        config = SkemaPackConfig(opt.ConfigFileName)
    except:
        print "No configuration file found. Try 'ImportSdeSkema.py --configfile=myconfig.cfg'"
        sys.exit(1)  
    print config 
    
    # 3) import from skema
    Events = ImportSdeSkema( config )
    
    # 4) output all events to stdout
    PrintEvents( Events )
    