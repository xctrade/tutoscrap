import mechanize

URL = "http://www.pagesjaunes.fr/"

def main():
	#create a browser instance
	b = mechanize.Browser()
	#load the page
	b.open(URL)
	#Select the form
	b.select_form(nr=0)
	#fill out the form
	b['quoiqui'] = "medecin"
	b['ou'] = "Paris"
	#Submit !
	return b.submit()

if __name__ == '__main__':
	import sys
	sys.stdout.write(main().read())
