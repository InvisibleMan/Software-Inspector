import urllib2, sys

#file_name = 'request.xml'
file_name = 'installed.programs.xml'

len = len(sys.argv)
if(len > 1):
	file_name = sys.argv[1]

with open(file_name, 'r') as f:
	xml_string = f.read()

#url = 'http://127.0.0.1:8000/api/programs'
url = 'http://2.homer.cz8.ru/api/programs'

req = urllib2.Request(url=url, 
					  data=xml_string, 
					  headers={'Content-Type': 'application/xml'})
try:
	resp = urllib2.urlopen(req)
except urllib2.URLError, e:
	#print dir(sys.exc_info()[0])
	#print(sys.exc_info()[0].__class__)
	#print e.code
	print e.read()
"""
except:
	print "Unexpected error:", sys.exc_info()[0]
	print dir(sys.exc_info()[0])
	print resp.read()
#	raise
"""
