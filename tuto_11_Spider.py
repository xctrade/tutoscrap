#spider
#!/usr/bin/python2.7
# -*-coding:Latin-1 -*
import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://mileycyrus.com"

urls = [url] # stack of urls
visited = [url] #historic of already visited urls

while len(urls)>0: # While is better since we will add new urls on the go
	try:	
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext)# parsing...

	urls.pop(0)
	print len (urls)
	for tag in soup.findAll('a',href=True): #findAll (with capital A) is a method OF Soup object ;) #href = True means there is actually a real link
		tag ['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])


print visited