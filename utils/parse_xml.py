import urllib2, sys
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLTreeBuilder

file_name = 'request.xml'
len = len(sys.argv)
if(len > 1):
	file_name = sys.argv[1]
else:
	raise Exception('No file-name')


#with open(file_name, 'rt') as f:
#    tree = ElementTree.parse(f)
#
#for node in tree.getiterator():
#    #print node.tag, node.attrib
#    dir(node.tag)
#    break
#
#
#exit(1)

class SoftwareItem(object):
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
            self.item = SoftwareItem()
            #print(self.item)
        
        #if tag != 'outline':
        #    # Ignore anything not part of the outline
        #    return
        #if not attrib.get('xmlUrl'):
        #    # Remember the current group
        #    self.group_name = attrib['text']
        #else:
        #    # Output a podcast entry
        #    self.writer.writerow( (self.group_name, attrib['text'],
        #                           attrib['xmlUrl'],
        #                           attrib.get('htmlUrl', ''),
        #                           )
        #                          )

    def end(self, tag):
        if tag == '{http://tempuri.org/DataSet1.xsd}InstalledSoftware':
            self.items.append(self.item)
            print(self.item)
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

target = InstalledSoftwareLoader()
parser = XMLTreeBuilder(target=target)
with open(file_name, 'rt') as f:
    for line in f:
        parser.feed(line)
parser.close()