import urllib2, sys
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLTreeBuilder
from www.models import SoftLine


class SoftwareItemDTO(object):
    name = ''
    version = ''
    is_removed = False
    is_hidden = False
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.version)

class InstalledSoftwareLoader(object):
    items = []
    item = None
    text = None
    
    def __init__(self):
        return

    def start(self, tag, attrib):
        #print(tag)
        if tag == '{http://tempuri.org/DataSet1.xsd}InstalledSoftware':
            self.item = SoftwareItemDTO()

    def end(self, tag):
        if tag == '{http://tempuri.org/DataSet1.xsd}InstalledSoftware':
            self.items.append(self.item)
            #print(self.item)
        elif tag == '{http://tempuri.org/DataSet1.xsd}sName':
            self.item.name = self.text
        elif tag == '{http://tempuri.org/DataSet1.xsd}sVersion':
            self.item.version = self.text
        elif tag == '{http://tempuri.org/DataSet1.xsd}bRemoved':
            self.item.is_removed = self.text
        elif tag == '{http://tempuri.org/DataSet1.xsd}bHidden':
            self.item.is_hidden = self.text
        pass
            
    def data(self, data):
        self.text = data

    def close(self):
        pass


def parse_xml(request):
	#print(request.POST)
	loader = InstalledSoftwareLoader()
	parser = XMLTreeBuilder(target=loader)
	parser.feed(request)
	#with open(file_name, 'rt') as f:
	#	for line in f:
	#		parser.feed(line)
	parser.close()
	SoftLine.objects.all().delete()
	for item in loader.items:
		line = SoftLine.objects.create(name = item.name, version = item.version)
		print("Item => '%s'\n" % item.name)

	return len(loader.items)
