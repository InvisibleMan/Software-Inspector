import urllib2, sys

print len(sys.argv)
exit("asdasd")

with open('installed.programs2.xml', 'r') as f:
    xml_string = f.read()

url = 'http://localhost:8080/'

req = urllib2.Request(url=url, 
                      data=xml_string, 
                      headers={'Content-Type': 'application/xml'})
urllib2.urlopen(req)