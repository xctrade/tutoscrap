#!/usr/bin/python2.7
# -*-coding:Latin-1 -*


#THIS TUTO SHOWS HOW TO GET DATAS FROM A WEB SITE AND DISPATCH THEM IN DIFFERENT FILES 

import urllib
import re
import json


#open a list of stockmarket symbols
symbolslist = open("symbols.txt","r").read()
symbolslist = symbolslist.split("\n") # for every new line, I have another item


################################Imprimer à l'ecran#####################################
"""
for symbol in symbolslist:
	URL = "http://www.bloomberg.com/markets/chart/data/1M/" + symbol +":US"
	htmltext = urllib.urlopen(URL).read()
	#print  htmltext


	data = json.load(urllib.urlopen(URL)) #warning json can only load a file not a string (=no "read")
	
	datapoints = data['data_values'] # we chose only the datavalues 
									 # (be careful not when the stock market is off)

	for point in datapoints:
		print "symbol",symbol,"time", point[0], "price", point[1]
"""
################################Imprimer dans un fichier#####################################
for symbol in symbolslist:
	save_results = open (symbol + ".txt", "w+") #create a new file for each loop
	save_results.close()

	URL = "http://www.bloomberg.com/markets/chart/data/1M/" + symbol +":US"
	htmltext = urllib.urlopen(URL).read()
	data = json.load(urllib.urlopen(URL)) #warning json can only load a file not a string (=no "read")
	datapoints = data['data_values'] # we chose only the datavalues 
									 # (be careful not when the stock market is off)



	save_results = open (symbol + ".txt", "a") # we append every lines (we dont want to have a file per data)
	for point in datapoints:
		save_results.write (str(symbol) + "," + str(point[0])+ "," + str(point[1]) + "\n")
	save_results.close()

