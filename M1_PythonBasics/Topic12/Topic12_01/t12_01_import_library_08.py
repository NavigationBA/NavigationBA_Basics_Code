import xml.dom.minidom
doc = xml.dom.minidom.parseString("<root><a>1</a></root>")
print(doc.documentElement.tagName)

import xml.etree.ElementTree as ET
root = ET.fromstring("<root><child>hi</child></root>")
print(root.tag)