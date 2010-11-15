# -*- coding: UTF-8 -*-
'''
Created on Nov 15, 2010

@author: pfl
'''
import unittest
import datetime
from Input.SkemaSum.SkemaSum import SumAppointments

SkemaDataBadCharsResult =  [
    {'Date': datetime.datetime(2010, 2, 17, 0, 0), 'Hours': [datetime.datetime(2010, 2, 17, 9, 0), datetime.datetime(2010, 2, 17, 9, 45)], 'Location': u'A-302æøåæøå', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP'}, 
    {'Date': datetime.datetime(2010, 2, 17, 0, 0), 'Hours': [datetime.datetime(2010, 2, 17, 10, 5), datetime.datetime(2010, 2, 17, 10, 50)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP'},
    {'Date': datetime.datetime(2010, 2, 17, 0, 0), 'Hours': [datetime.datetime(2010, 2, 17, 10, 55), datetime.datetime(2010, 2, 17, 11, 40)], 'Location': u'A-302', 'Class': u'10OIT2bH1æøåæøå', 'Subject': u'Netvxrk/OOP'},
    {'Date': datetime.datetime(2010, 2, 19, 0, 0), 'Hours': [datetime.datetime(2010, 2, 19, 9, 0), datetime.datetime(2010, 2, 19, 9, 45)], 'Location': u'A-302æøåæøå', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP'}, 
    {'Date': datetime.datetime(2010, 2, 20, 0, 0), 'Hours': [datetime.datetime(2010, 2, 20, 10, 5), datetime.datetime(2010, 2, 20, 10, 50)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP'},
    {'Date': datetime.datetime(2010, 2, 15, 0, 0), 'Hours': [datetime.datetime(2010, 2, 15, 10, 55), datetime.datetime(2010, 2, 15, 11, 40)], 'Location': u'A-302', 'Class': u'10OIT2bH1æøåæøå', 'Subject': u'Netvxrk/OOP'},
    ]

class Test(unittest.TestCase):
    ''' SkemaSum '''

    def setUp(self):
        self.skemaSum = SumAppointments()
        for appointment in SkemaDataBadCharsResult:
            self.skemaSum.addAppointment(appointment)
        pass


    def tearDown(self):
        pass


    def testSumByDay(self):
        ''' SkemaSum : sumByDay - test start date''' 
        self.assertEqual(self.skemaSum.sumByDay()[0],  datetime.datetime(2010, 2, 15, 0, 0).date(), "Start date is not correct.")
        self.assertEqual(self.skemaSum.sumByDay()[1], 6, 'the length of the array is wrong')
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()