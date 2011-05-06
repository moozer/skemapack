'''
Created on May 6, 2011

@author: morten
'''

import unittest, os
from Datatypes.ActivityDb import ActivityDb


class Test(unittest.TestCase):
    def setUp(self):
        self._StartDir = os.getcwd()
        this_dir = os.path.dirname( __file__ )
        while 1 == 1:
            this_dir, tail = os.path.split( this_dir )
            if tail == 'src': # always go to src as default dir.
                this_dir = os.path.join( this_dir, tail )
                break
        os.chdir( this_dir )
        
        try: # if it fails, then we are in the correct directory.
            os.chdir(".")
        except:
            pass
        
    def tearDown(self):
        os.chdir(self._StartDir )
        pass

    def testConstructor(self):
        db = ActivityDb(':memory:')
        self.assertTrue( len( db.getMetadata() ) > 0 )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()