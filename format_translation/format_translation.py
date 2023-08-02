# translating an xml file to json, creating new json

import json
import xmltodict

with open("People.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

    json_data = json.dumps(data_dict)

with open("People.json", "w") as json_file:
    json_file.write(json_data)
