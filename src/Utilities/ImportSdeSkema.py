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
        print event
    
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
              'FirstWeek': 35,
              'LastWeek': 52,
              'Year': 2011,
              'Dateformat': "%d-%m-%Y"
              }
    #python ~/bin/SkemaOnCron.py -I 5421 -n 5 -d ~/bin/ics

    # 2) output config
    PrintConfig( config )
    
    # 3) import from skema
    Events = ImportSdeSkema( config )
    
    # 4) output all events to stdout
    PrintEvents( Events )
    