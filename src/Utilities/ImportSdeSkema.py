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
def PrintEvents( events, config ):
    for event in events:
        print "%s: %s; "%('Date', event['Date'].strftime(config['OutputDateformat'])),
        print "%s: %s; "%('StartTime', event['Hours'][0]),
        print "%s: %s; "%('EndTime', event['Hours'][1]),
        print "%s: %s; "%('Location', event['Location']),
        print "%s: %s; "%('Class', event['Class']),
        print "%s: %s; "%('Subject', event['Subject']),
        print "" # adding final newline
    
def ImportSdeSkema( config ):
    myLoader = loadWeb.htmlGetter()
    Data = myLoader.getSkemaWithPost(config['TeacherId'], config['FirstWeek'], config['LastWeek'], config['Year']).read()

    # TODO: 'data' field in appointments is wrong.
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
              'Dateformat': "%d-%m-%Y",
              'OutputDateformat': '%Y-%m-%d'
              }
    
    # 3) import from skema
    Events = ImportSdeSkema( config )

    config['Dateformat'] = config['OutputDateformat']

    # 2) output config
    PrintConfig( config )
    
    # 4) output all events to stdout
    PrintEvents( Events, config )
    