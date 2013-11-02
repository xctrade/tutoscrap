import urllib2
import urllib
from bs4 import BeautifulSoup

# The URL to this service
URL = 'http://www.leboncoin.fr/annonces/offres/ile_de_france/'
#http://www.leboncoin.fr/animaux/offres/ile_de_france/?f=a&th=1&ps=0&pe=13&q=chat&location=Vincennes%2094300

def main():
    # Here is the data that FireBug said we sent
    postdict = {'q' : 'chien',
                'location' : 'Vincennes',
                'ps' : '1', # Prix min=> en fonction du menu deroulant e.g- 13 == 1000€ 14 == 2500€
                'pe' : '13', # Prix max=> en fonction du menu deroulant e.g- 13 == 1000€ 14 == 2500€
                'f':'a'}

    # Encode it into HTTP form, permet de transformer les parametres en lanagage http
    postme = urllib.urlencode(postdict)

    # Send it...
    fd = urllib2.urlopen(URL, postme)
    return fd
    