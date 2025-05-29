import xmltodict

with open('data/r1.xml') as file: # Open the XML file
    xml_content = file.read()# Read the content of the file
    data = xmltodict.parse(xml_content)

data = xmltodict.parse(xml_content)  # Parse the XML content into a dictionary

print(data['router']['interfaces']['interface'][0]['ip'])  # Print the parsed data
print(data)