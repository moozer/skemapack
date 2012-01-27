'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Datatypes.EventFunctions import WriteEvents
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys


def ImportSdeSkema( config, ConfigSet = "SkemaScraper" ):
    # read data from file or net
    if config.get(ConfigSet, "Infile"):
        Data = open(config.get(ConfigSet, "Infile")).read()
    else:
        myLoader = loadWeb.htmlGetter()
        Data = myLoader.getSkemaWithPost(config.get(ConfigSet, "TeacherId"), 
                                     config.get(ConfigSet, "FirstWeek"), 
                                     config.get(ConfigSet, "LastWeek"), 
                                     config.get(ConfigSet, "Year")).read()
                                     
    # and process data
    parser = SdeSkemaScraper( config.get(ConfigSet, "InputDateformat") )
    parser.feed( Data )
    parser.close()
    
    # TODO: Decide on name for this, Appointments or Events
    return  parser.Appointments 


if __name__ == '__main__':

    if len(sys.argv) > 2:
        cfgfile = sys.argv[1]
    else:
        cfgfile = SkemaPackConfig_stdin()

#    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "SkemaScraper"

    # 3) import from skema
    Events = ImportSdeSkema( config, ConfigSet )
    
    # 4) output all events to stdout
    print config # placed here to allow config to be changed...
    WriteEvents( Events, config, ConfigSet )
    