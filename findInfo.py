import rhinoscriptsyntax as rs
import json

#prompt the user for a file to import
filter = "JSON file (hallgrimskirkja.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
if filename:
    with open(filename, "r") as f:
        data = json.load(f)

#Use the new datastore datastructure    
print(data)

#print(json.dumps(f,indent=4, sort_keys=description))
#print(data.Demo.value[description])


#datastore = json.loads(json_string)