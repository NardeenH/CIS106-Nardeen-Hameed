import urllib.request
import xml.etree.ElementTree

url = "http://www.w3schools.com/xml/note.xml"
try:
    page = urllib.request.urlopen(url).read()
    page = page.decode("UTF-8")
except Exception as exception:
    print(str(exception) + " reading " + url)
    exit(1)

root = xml.etree.ElementTree.fromstring(page)
tree = xml.etree.ElementTree.ElementTree(root)

for element in tree.iter():
    print("%s: %s" % (element.tag, element.text))