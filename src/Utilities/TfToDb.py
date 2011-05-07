'''
Created on May 7, 2011

@author: morten
'''

from optparse import OptionParser
from Input.TfImporter.TfCsvImport import TfCsvImport
from Input.TfImporter.TfExtraCsvImport import TfExtraCsvImport
from Datatypes.ActivityDb import ActivityDb

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", default = None,
                      help="Location of TF csv file to read", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="out.sqlite", 
                      help="Filename of database file", metavar="OUTFILE")
    parser.add_option("-x", "--extrafile", dest="extrafile", default = None,
                      help="Extra csv data to include", metavar="EXTRAFILE")
    parser.add_option("-d", "--basedb", dest="basedb", default="BaseDb.sql",
                      help="path to the sql file using for initializing the database", metavar="BASEDB")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


if __name__ == '__main__':
    opt = ParseCmdLineOptions()

    # file stuff
    print "Loading CSV file:%s"%opt.infile
    tfi = TfCsvImport( opt.infile )
        
    if opt.extrafile:
        print "Loading extra CSV file:%s"%opt.extrafile
        tfix = TfExtraCsvImport( opt.extrafile )
    else:
        tfix = None

    print "Using db file %s" % opt.outfile        
    db = ActivityDb( opt.outfile, opt.basedb )
    
    # Do the data movement.
    tfi.EnableImportAll()

    i = 0    
    for Activity in tfi:
        i = i+1
        db.AddActivity(Activity)
        
    print "Done inserting data in DB %d entries inserted" % i
