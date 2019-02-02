import rhinoscriptsyntax as rs
import json

#prompt the user for a file to import
filter = "JSON file (hallgrimskirkja.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

#Use the new datastore datastructure
#print datastore["office"]["parking"]["style"]
#print datastore ["Demo"]["value"]
print(datastore["Demo"])


#datastore = json.loads(json_string)