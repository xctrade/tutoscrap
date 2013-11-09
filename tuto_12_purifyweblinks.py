#purify my links
#!/usr/bin/python2.7
# -*-coding:Latin-1 -*
import urllib
from bs4 import BeautifulSoup
import urlparse

#on met au propre les adresses
#on collecte les hostnames et les paths pour les recoller

htmltext = urllib.urlopen("http://www.nytimes.com")
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a',href=True):
	raw = tag['href']
	b2 = urlparse.urlparse(tag['href']).path
	b1 = urlparse.urlparse(tag['href']).hostname

	print str(b1) +str(b2)
