'''
Created on Jul 12, 2011

@author: morten
'''

from Other.PythonPathUtil import AppendSrcToPythonPath
AppendSrcToPythonPath()

from optparse import OptionParser
from Input.TfImporter.TfCsvImport import TfCsvImport
from Input.TfImporter.TfExtraCsvImport import TfExtraCsvImport
from Datatypes.ActivityDb import ActivityDb

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-d", "--basedir", dest="BaseDir", default = '.',
                      help="Location of TF directories")
    parser.add_option("-v", "--tfversion", dest="Version", default = None,
                      help="Versionstring to use")
#    parser.add_option("-o", "--outfile", dest="outfile", default="out.sqlite", 
#                      help="Filename of database file", metavar="OUTFILE")
#    parser.add_option("-x", "--extrafile", dest="extrafile", default = None,
#                      help="Extra csv data to include", metavar="EXTRAFILE")
#    parser.add_option("-d", "--basedb", dest="basedb", default=None,
#                      help="path to the sql file using for initializing the database", metavar="BASEDB")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


import sys, os, shutil, zipfile


def ExtractVersionString( VersionString ):
    if not VersionString:
        print "Please supply version identifier (ex. 0.09)"
        VersionString = sys.stdin.readline()
    else:
        VersionString = VersionString
    
    return VersionString


def ExtractZipFileToUse(BaseDir):
    files = os.listdir(BaseDir)
    zipfiles = [file for file in files if os.path.splitext(file)[1] == '.zip']
    if len(zipfiles) == 0:
        print "no .zip files found in %s" % (BaseDir, )
        exit()
    for i, filename in enumerate(zipfiles):
        print "%s: %s" % (i, filename)
    
    valid_input = 0 # we haven't gotten valid input yet
    while not valid_input:
        try:
            x = int(raw_input("Enter an integer: "))
            if x in range(0, len(zipfiles)):
                valid_input = 1
            else:
                print "please supply value between 0 and %i" % (len(zipfiles) - 1, )
        except ValueError as err:
            print "'%s' is not a valid integer." % err.args[0].split(": ")[1]
    
    return os.path.join( BaseDir, zipfiles[x] )


def CreateSubdirs(Directories):
    for Dir in Directories.keys():
        if os.path.isdir(Directories[Dir]):
            print "%s exists - skipping" % (Directories[Dir], )
        else:
            print "Creating diretory %s" % (Directories[Dir], )
            os.makedirs(Directories[Dir])


def MoveAndUnzip(zipfilename, Directories):
    zipfile_new = os.path.join(Directories['Raw'], os.path.split(zipfilename)[1])
    print "moving zip file from %s to %s" % (zipfilename, zipfile_new) #    shutil.move( zipfilename, zipfile_new)
    shutil.copy(zipfilename, zipfile_new)
    TfZip = zipfile.ZipFile(zipfile_new)
    print "files in archive"
    files = TfZip.namelist()
    print files
    TfZip.extractall(Directories['Raw'])
    return files

def  main():
    print "Tf zip importer."
    opt = ParseCmdLineOptions()
    print "commandLine options:"
    print opt
    
    # Get version number from user
    VersionString = ExtractVersionString( opt.Version )
    TfDir = "TF_2011_%s" % (VersionString,)
    print "Using version %s and sub dir %s" %(VersionString, TfDir)
    
    # list zip file and choose which to move
    zipfilename = ExtractZipFileToUse(opt.BaseDir)    
    print "The user chose %s" % (zipfilename,)
    
    # Create directories
    Directories= {  'Raw'  : os.path.join( opt.BaseDir, "%s/Raw"%TfDir ),
                    'Html' : os.path.join( opt.BaseDir, "%s/Html"%TfDir ),
                    'Database': os.path.join( opt.BaseDir, "%s/DB"%TfDir ),
                    'Temp'    : os.path.join( opt.BaseDir, "%s/Temporary"%TfDir ) }
    CreateSubdirs(Directories)
    
    # move and unzip
    files = MoveAndUnzip(zipfilename, Directories)

    # spawn libreoffice as a convenience for the user    
    Cmd = "libreoffice"
    for file in files:
        Cmd = "%s %s"%(Cmd, "\"%s\""%os.path.join(Directories['Raw'], file))
    print "issuing: %s"%Cmd
    os.system( Cmd )

    # ask user to export csv with correct name
    CsvFiles = {    "Autumn": os.path.join( Directories['Temp'], "2011A_IT-skema.csv"), 
                    "Spring": os.path.join( Directories['Temp'], "2011S_IT-skema.csv") }
    
    for str in CsvFiles.keys():
        while not os.path.isfile(CsvFiles[str]):
            print "File not found %s"%CsvFiles[str]
            raw_input( "Extract ITET lesson plan from the xls file and press enter" )
    
    # TfToDb with proper parameters
    SqlFiles =  {   "Autumn": os.path.join( Directories['Database'], "TF_2011A.sqlite"), 
                    "Spring": os.path.join( Directories['Database'], "TF_2011S.sqlite") }
    
    for str in SqlFiles.keys():
        if os.path.isfile(SqlFiles[str]):
            print "Database already exists. backing up."
            shutil.move(SqlFiles[str], "%s.bak"%SqlFiles[str])
        Cmd = "python ~/bin/TfToDb.py -i \"%s\" -o \"%s\"" %(CsvFiles[str],SqlFiles[str])
        os.system(Cmd)

    
    # DbToHtml for chosen version
    HtmlDirs = {    "Autumn": os.path.join( Directories['Html'], "Autumn" ), 
                    "Spring": os.path.join( Directories['Html'], "Spring") }
    HtmlPrefix = {  "Autumn": "TF_2011A_", "Spring": "TF_2011S_" }
    for str in SqlFiles.keys():
        os.mkdir( HtmlDirs[str])
        Cmd = "python ~/bin/DbToCmpHtml.py -i \"%s\" -d \"%s\" -o \"%s\""%(SqlFiles[str], HtmlDirs[str], HtmlPrefix[str])
        os.system(Cmd)

    # Ask user for version to compare with
    # TBD
    
    print "Done importing"
    
if __name__ == '__main__':
    main()