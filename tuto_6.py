import urllib
import re
import json

# open the web page
URL = "http://www.bloomberg.com/markets/chart/data/1M/AAPL:CI"
htmltext = urllib.urlopen(URL).read()
print  htmltext



data = json.load(urllib.urlopen(URL)) #warning json can only load a file not a string (=no "read")

datapoints = data['data_values'] # we chose only the datavalues 
								 # (be careful not when the stock market is off)

for point in datapoints:
	print point [1]

print "the number of points(days) is", len(datapoints)
datapoints[len(datapoints)-1][1]
