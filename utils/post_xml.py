import urllib, urllib2, sys

file_name = 'request.xml'
#file_name = 'installed.programs.xml'

len = len(sys.argv)
if(len > 1):
	file_name = sys.argv[1]

with open(file_name, 'r') as f:
	xml_string = f.read()

#url = 'http://2.homer.cz8.ru/api/programs'
url_login = 'http://127.0.0.1:8000/login/'
url_api = 'http://127.0.0.1:8000/api/programs'
url_index = 'http://127.0.0.1:8000'

#req = urllib2.Request(url=url, 
#					  data=xml_string, 
#					  headers={'Content-Type': 'application/xml'})

params = urllib.urlencode(dict(username='Nikolay', password='1'))
#print params
#exit()

try:
#	resp = urllib2.urlopen(req)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	urllib2.install_opener(opener)
	f = opener.open(url_login, params)
	#data = f.read()
	f.close()
	f = opener.open(url_api, xml_string)
	data = f.read()
	f.close()
	#print (len(xml_string))
	print(data)
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
