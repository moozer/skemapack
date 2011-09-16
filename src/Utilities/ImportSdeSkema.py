'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Configuration.CommandLineOptions import ReadOptions

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
    
#    # 1) read config/parameter
    # 3) import from skema
    Events = ImportSdeSkema( ReadOptions() )
    
    # 4) output all events to stdout
    PrintEvents( Events )
    