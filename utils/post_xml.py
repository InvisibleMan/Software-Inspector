import urllib2, sys

file_name = 'request.xml'
len = len(sys.argv)
if(len > 1):
	file_name = sys.argv[1]

with open(file_name, 'r') as f:
    xml_string = f.read()

url = 'http://127.0.0.1:8000/api/programs'

req = urllib2.Request(url=url, 
                      data=xml_string, 
                      headers={'Content-Type': 'application/xml'})
urllib2.urlopen(req)