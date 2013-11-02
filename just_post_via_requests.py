import requests

# The URL to this service
URL = 'http://www.leboncoin.fr/annonces/offres/ile_de_france/'
#http://www.leboncoin.fr/animaux/offres/ile_de_france/?f=a&th=1&ps=0&pe=13&q=chat&location=Vincennes%2094300

def main():
    # Here is the data that FireBug said we sent
    postdict = {
                'f':'a',
                'th' : "0",
                'q' : 'chien',
                'ur' :"1",
                'location' : 'Vincennes'
                }

    # Encode it into HTTP form, permet de transformer les parametres en lanagage http
    fd = requests.post(URL, data=postdict)

    # Send it...
    print fd
