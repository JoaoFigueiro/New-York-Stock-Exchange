import xml.etree.ElementTree

xml_file = 'files/nyse.xml'

try: 
    nyse = xml.etree.ElementTree.parse(xml_file).getroot()
except FileNotFoundError: 
    print('File not Found!')
    exit(1)
except xml.etree.ElementTree.ParseError:
    print("Stock data file contains invalid data")
    exit(2)

key_names = ["COMPANY", "LAST", "CHANGE", "MIN", "MAX"]
key_widths = [50, 10, 10, 10, 10]

for (n, w) in zip(key_names, key_widths):
    print(n.ljust(w), end=' ')

print()    
print('-'*95)

for elements in nyse: 
    print(
        elements.text.ljust(50),
        elements.attrib.get("last").ljust(10),
        elements.attrib.get("change").ljust(10),
        elements.attrib.get("min").ljust(10),
        elements.attrib.get("max").ljust(10), sep=' '
    )
