'''
Created on Sep 13, 2011

@author: morten
'''

from Input.HtmlScraper.DalumSkemaScraper import DalumSkemaScraper
from Configuration.CommandLineOptions import ReadOptions
from Datatypes.EventFunctions import WriteEvents
from datetime import date, datetime, timedelta
    
def ImportDalumSkema( config, ConfigSet = "DalumSkema" ):
    now = date.today()
    
    # getting reference date
    BaseWeek = int(config.get( ConfigSet, 'BaseWeek' ))
    if BaseWeek == 0:
        BaseDate = now
    else:
        BaseDate = date.strptime("%s %s" % (now.year, BaseWeek, "%Y %W") )
    
    # the week range
    WeekOffset = int( config.get( ConfigSet, 'Offset' ) )
    WeekCount =  int( config.get( ConfigSet, 'NumWeeks' ) )
    
    config.get( ConfigSet, 'BaseWeek' )
    StartDate = BaseDate + timedelta(weeks=WeekOffset)
    EndDate = BaseDate + timedelta(weeks=WeekOffset+WeekCount)

    if StartDate.year != EndDate.year:
        raise ValueError( "Data extraction across new year not implemented" )
    
    WeekRange = range( StartDate.isocalendar()[1], EndDate.isocalendar()[1] )

    # and extract stuff
    s = DalumSkemaScraper( int(config.get( ConfigSet, 'TeacherId' )), WeekRange )
    s.ExtractAppointments( NonFatal = True )
    Apps = s.GetAppointments()
    return Apps
#    myLoader = loadWeb.htmlGetter()
#    Data = myLoader.getSkemaWithPost(config.get(ConfigSet, "TeacherId"), 
#                                     config.get(ConfigSet, "FirstWeek"), 
#                                     config.get(ConfigSet, "LastWeek"), 
#                                     config.get(ConfigSet, "Year")).read()
#    parser = SdeSkemaScraper( config.get(ConfigSet, "InputDateformat") )
#    parser.feed( Data )
#    parser.close()
    
    # TODO: Decide on name for this, Appointments or Events
#    return  parser.Appointments 


if __name__ == '__main__':
    
#    # 1) read config/parameter
    config = ReadOptions( Silent = True )

    # 3) import from skema
    ConfigSet = "DalumSkema"
    Events = ImportDalumSkema( config, ConfigSet )
    
    # 4) output all events to stdout
    print config # placed here to allow config to be changed...
    WriteEvents( Events, config, ConfigSet )
    