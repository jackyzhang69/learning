import json

# Dictionary to json
appDict = {
  'name': 'messenger',
  'playstore': True,
  'company': 'Facebook',
  'price': 100
}
app_json = json.dumps(appDict) # dict ->json string. app_json is a json string
print(app_json)

json_obj=json.loads(app_json) # convert json string to json object
print(json_obj)

for k, v in json_obj.items(): # iterate through json items methods
    print(k+": "+str(v))

# Write json to a file

with open ('json\\app.txt','w') as json_file:
    json.dump(json_obj,json_file)

