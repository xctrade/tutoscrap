# Pour POSTer on peut utiliser urllib ou mechanize ou  request
import mechanize
# The URL to this service
URL = 'hhttp://www.leboncoin.fr/annonces/offres/ile_de_france/'


def main():
    # Create a Browser instance
    b = mechanize.Browser()
    #disable loading robot.txt to avoid getting a 403 robot error
    b.set_handle_robots(False)
     # can sometimes hang without this
    b.set_handle_refresh(False) 

    b.addheaders = [('User-agent',
                 'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)')]

    # Load the page
    b.open(URL)
    # Select the form
    b.select_form(nr=0)
    # Fill out the form
    b['f'] = 'a'
    b['th'] = '0'
    b['q'] = 'chien'
    b['ur'] = '1'
    b['location'] = 'Vincennes'

    # Submit!
    return b.submit()


# Attention erreur classique => erreur 403 disallowed to robots 
if __name__ == '__main__':
	import sys
	sys.stdout.write(main().read())
