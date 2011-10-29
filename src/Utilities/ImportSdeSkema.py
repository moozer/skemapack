'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Configuration.CommandLineOptions import ReadOptions
from Datatypes.EventFunctions import WriteEvents
    
def ImportSdeSkema( config, ConfigSet = "SkemaScraper" ):
    myLoader = loadWeb.htmlGetter()
    Data = myLoader.getSkemaWithPost(config.get(ConfigSet, "TeacherId"), 
                                     config.get(ConfigSet, "FirstWeek"), 
                                     config.get(ConfigSet, "LastWeek"), 
                                     config.get(ConfigSet, "Year")).read()
    parser = SdeSkemaScraper( config.get(ConfigSet, "InputDateformat") )
    parser.feed( Data )
    parser.close()
    
    # TODO: Decide on name for this, Appointments or Events
    return  parser.Appointments 


if __name__ == '__main__':
    
#    # 1) read config/parameter
    config = ReadOptions()

    # 3) import from skema
    Events = ImportSdeSkema( config )
    
    # 4) output all events to stdout
    print config # placed here to allow config to be changed...
    WriteEvents( Events, config, "SkemaScraper" )
    