#Web Crawl
#!/usr/bin/python2.7
# -*-coding:Latin-1 -*
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

#we just add a stack/queue to the last tutorial

url = "http://www.sparkbrowser.com"
br = mechanize.Browser() #mechanize create a virtual browser
br.open(url)

urls = [url]
visited =[url]
while len (urls)>0:
	try:
		br.open(urls[0])
		urls.pop(0)
		for link in br.links(): #mechanize has a method links, let"s parse the result of it
			newurl = urlparse.urljoin(link.base_url,link.url)
			b1 = urlparse.urlparse(newurl).hostname # to be sure to have a proper link
			b2 = urlparse.urlparse(newurl).path
			newurl = "http://" +b1+b2

			if newurl not in visited and urlparse.urlparse(url).hostname in newurl:#to be sure we don't browse external links
				visited.append(newurl)
				urls.append(newurl)
				print newurl
	except:
		print "erreur!"

