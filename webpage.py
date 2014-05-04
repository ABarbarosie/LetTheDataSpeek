import urllib
import urllib2
import mechanize
import time
import cookielib

class WebPage:
    def __init__(self, words):
        base = "http://www.google.com/trends/trendsReport?q="
        terminate = "&export=1"
        separator = ",+"

        if len(words) == 1:
            self.link = base + words[0] + terminate
        elif len(words) > 1:
            self.link = base
            for i in range(0, len(words) - 1):
                self.link += words[i] + separator
            self.link += words[len(words) - 1] + terminate
        else:
            self.link = ""

    def getContent(self):
        br = mechanize.Browser()

        # Act like we're a real browser
        br.set_handle_robots(False)
        br.set_handle_equiv(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        
        response = br.open('https://accounts.google.com/ServiceLogin?hl=en&continue=https://www.google.com/')
        
        forms = mechanize.ParseResponse(response)
        form = forms[0]
        form['Email'] = 'letthedataspeak'
        form['Passwd'] = 'Ilovemagic!'
        
        response = br.open(form.click())
        time.sleep(5)
        
        intermediate = br.open(self.link)

        self.content = intermediate.read()
