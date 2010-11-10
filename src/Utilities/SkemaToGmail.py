'''
Created on Nov 9, 2010

@author: pfl
'''

#from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile
from Output.IcsOutput.IcsOutput import IcsOutput
import Input.HtmlGetter.loadWebPage.loadHtml as HtmlGetter
from Input.HtmlScraper.BeautifulSkemaScraper import  BeautifulSkemaScraper

from Output.Calendar.Gmail.gmailOutput import GmailOutput

def ParseCmdLineOptions():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-n", "--user", dest="user",
                      help="Gmail user name", metavar="USER")
    parser.add_option("-p", "--passwd", dest="pw",
                      help="Gmail password", metavar="PW")
    parser.add_option("-u", "--url", dest="url", default="http://skema.sde.dk/laerer/3735/en-US.aspx",
                      help="Skema url", metavar="URL")
    
    parser.add_option( "-i", "--interface", dest="interface", default="cli",
                      help="Interface cli or api", metavar="CLI")
    
    (options, args) =  parser.parse_args()
    return options


def main():
    opt = ParseCmdLineOptions()
    
    print (opt.user)
    print (opt.pw)
    print (opt.url)
    print (opt.interface)
    
    myHtmlGetter = HtmlGetter.htmlGetter()
    htmlResponse = myHtmlGetter.getSkemaWithPost(3735,43,44)
    
    htmlScraper = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
    htmlScraper.feed(htmlResponse.read())
    
    myGmailOutput = GmailOutput("poul.flindt.skema","minmine1")
    
    
    for Appointment in htmlScraper.Appointments:
        myGmailOutput.addAppointment(Appointment)
    
    
    return 0

if __name__ == '__main__': main()
