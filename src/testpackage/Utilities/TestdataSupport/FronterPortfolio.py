'''
Created on May 16, 2011

@author: morten
'''


PortfolioFilename = 'FronterPortfolio/AnonTestData.html'
PortfolioStudents = [
    {'Name': u'test20, test20', 'Include': True}, {'Name': u'test22, test22', 'Include': True}, 
    {'Name': u'Test4, Test4', 'Include': True}, {'Name': u'Test5, Test5', 'Include': True}, 
    {'Name': u'Test6, Test6', 'Include': True}, {'Name': u'Test9, Test9', 'Include': True}]

PortfolioHandins = [
    u'try', u'ProNet Report hand-in', u'SD mini project', 
    u'SD Presentations', u'SD RC car', u'PP_w50']

PortfolioHandinsFirstStudent = {
    u'SD RC car': {'Course': u'SD', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'SD mini project': {'Course': u'SD', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'ProNet Report hand-in': {'Course': u'ProNet', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}, 
    u'try': {'Course': u'try', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'PP_w50': {'Course': u'PP_w50', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'SD Presentations': {'Course': u'SD', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}}
PortfolioHandinsSecondStudent = {
    u'SD RC car': {'Course': u'SD', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}, 
    u'SD mini project': {'Course': u'SD', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}, 
    u'ProNet Report hand-in': {'Course': u'ProNet', 'Evaluation': u'Not approved', 'Pending': False, 'Missing': True}, 
    u'try': {'Course': u'try', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'PP_w50': {'Course': u'PP_w50', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'SD Presentations': {'Course': u'SD', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}}
PortfolioHandinsThirdStudent = {
    u'SD RC car': {'Course': u'SD', 'Evaluation': u'In progress', 'Pending': True, 'Missing': False}, 
    u'SD mini project': {'Course': u'SD', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}, 
    u'ProNet Report hand-in': {'Course': u'ProNet', 'Evaluation': u'In progress', 'Pending': True, 'Missing': False}, 
    u'try': {'Course': u'try', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'PP_w50': {'Course': u'PP_w50', 'Evaluation': u'Not delivered', 'Pending': False, 'Missing': True}, 
    u'SD Presentations': {'Course': u'SD', 'Evaluation': u'Approved', 'Pending': False, 'Missing': False}}
