import urllib
import urllib2

class WebPage:
	def __init__(self, words):
		base = "http://www.google.com/trends/explore#q="
		terminate = "&cmpt=q"
		separator = "%2C"
		if len(words) == 1:
			self.link = base + words[0] + terminate
		elif len(words) > 1:
			self.link = base
			for i in range(0,len(words)-1):
				self.link += words[i] + separator
			self.link += words[len(words)-1] + terminate 
		else:
			self.link = ""

	def getContent(self):
		intermediate = urllib2.urlopen(self.link)
		self.content = intermediate.read()
