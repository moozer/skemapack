'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb

# TODO: move to file that contains general import/export supprt functions
def PrintConfig( configdict ):
    print "## Configuration used"
    for entry in configdict.keys():
        print "# %s = %s"%(entry, configdict[entry])
    print "#"
    
# TODO: move to support file
# TODO: Eventes should be a data type with event.__str__()
def PrintEvents( events ):
    for event in events:
        for key in event.keys():
            print "%s: %s; "%(key, event[key]),
        print "" # adding final newline
    
def ImportSdeSkema( config ):
    myLoader = loadWeb.htmlGetter()
    Data = myLoader.getSkemaWithPost(config['TeacherId'], config['FirstWeek'], config['LastWeek'], config['Year']).read()
    parser = SdeSkemaScraper( config['Dateformat'] )
    parser.feed( Data )
    parser.close()
    
    return  parser.Appointments 


if __name__ == '__main__':
    # 1) read config/parameter
    config = { 
              'TeacherId': 5421,
              'FirstWeek': 33,
              'LastWeek': 52,
              'Year': 2011,
              'Dateformat': "%d-%m-%Y"
              }

    # 2) output config
    PrintConfig( config )
    
    # 3) import from skema
    Events = ImportSdeSkema( config )
    
    # 4) output all events to stdout
    PrintEvents( Events )
    