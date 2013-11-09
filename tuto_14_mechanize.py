#mechanize
#!/usr/bin/python2.7
# -*-coding:Latin-1 -*
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

#The main idea here is to build a crawler that can open all pages in a specific order without looping
#We test it on a "on purpose" website that features an easy to test  architecture cf.xiaohld.com/test


url = "http://www.travelercar.com"
br = mechanize.Browser() #mechanize create a virtual browser
br.open(url)

for link in br.links(): #mechanize has a method links, let"s parse the result of it
	newurl = urlparse.urljoin(link.base_url,link.url)
	b1 = urlparse.urlparse(newurl).hostname # to be sure to have a proper link
	b2 = urlparse.urlparse(newurl).path
	print "http://" +b1+b2

	#print "the base url is: " + link.base_url
	#print "the url is: " + link.url


"""
base = "http://www.xiaohld.com/"
htmlfile  = urllib.urlopen (url)
soup = BeautifulSoup(htmlfile)

for tag in soup.findAll('a',href=True):
	print base+tag['href']
"""


