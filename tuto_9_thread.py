#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from threading import Thread
import urllib
import re
#Python threads are used in cases where the execution of a task involves some waiting. One example would be interaction with a service hosted on another computer, such as a webserver. Threading allows python to execute other code while waiting; this is easily simulated with the sleep function.
#3 steps to use your computer memory multitask (thread)
#		 for printing all stock exchange values
# 1) test opening, reading the webpages (100 first words)
# 2) test the regex, just print the title
# 3) insert the stock symbol

gmap = {}#gmap permet de garder un ordre dans la lecture du résultat car le multi thread amene les résultats dans le désordre

def mythread (myurl):
	base = "http://fr.finance.yahoo.com/q?s="+myurl
	regex = '<span id="yfs_l84_'+myurl.lower()+'">(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern, htmltext)
	#print "the price of "+ str(myurl)+ " is "+ str(results)
	try :
		gmap[myurl] = results[0] #we simply associate the value collected
	except:
		print "got an error"


symbolslist = open ("C://users/xcpro/desktop/github/tutoscrap/symbols.txt").read()
symbolslist = symbolslist.split("\n")
print symbolslist
threadlist = [] # list to collect datas and append it 

for u in symbolslist:
	t = Thread(target=mythread,args=(u,))
	t.start()
	threadlist.append(t)#(will be appended in random order = thread)

for b in threadlist:
	b.join() #join "pause" the next action of the main thread until all child thread (here every stock collecting action) are finished

for key in gmap.keys():
	print key, gmap[key]

