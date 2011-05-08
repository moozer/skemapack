'''
Created on May 8, 2011

@author: morten
'''

import os

ScriptDir = "testpackage/Utilities"
TempDataDir= ScriptDir + "/tempdata" 

def CloneTestData():
    StartDir = ChDirToSrc()
    os.chdir(ScriptDir)
    if os.system('sh CloneTestData.sh'):
        raise IOError("CloneTestData.sh not found in %s" % os.getcwd())
    os.chdir( StartDir )

def RemoveTestData():
    ''' runs the cleanup script. cwd i scriptdir after function call '''
    ChDirToSrc()
    os.chdir(ScriptDir)
    os.system('sh RemoveTestData.sh')

def ChDirToSrc():
    ''' Chdir to the src directory. This is to give a known base line '''
    InitialDir = os.getcwd()
    this_dir = InitialDir
    while 1 == 1:
        this_dir, tail = os.path.split(this_dir)
        if tail == 'src': # always go to src as default dir.
            this_dir = os.path.join(this_dir, tail) 
            break
                
    os.chdir(this_dir)
    return InitialDir
