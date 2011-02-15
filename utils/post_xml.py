<<<<<<< HEAD
import urllib2, sys

print len(sys.argv)
exit("asdasd")

with open('installed.programs2.xml', 'r') as f:
    xml_string = f.read()

url = 'http://localhost:8080/'

req = urllib2.Request(url=url, 
                      data=xml_string, 
                      headers={'Content-Type': 'application/xml'})
=======
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
>>>>>>> 92f3c7c3f131be45e62c36ffe7d6aaee67bb81da
urllib2.urlopen(req)