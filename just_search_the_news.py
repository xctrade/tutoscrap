import mechanize
import os

URL = "http://www.lemonde.fr/"

def is_there_word():
	#create a browser instance
	b = mechanize.Browser()
	#load the page
	fd = b.open(URL)
	#return the word I choose eg. "Halloween"
	return "vabre" in fd.read().lower()

if __name__ == '__main__':
	if is_there_word():
		print "yes"
	else :
		print"no"
	input("appuyer sur une touche pour terminer")

