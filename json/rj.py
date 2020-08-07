#!~/venv/bin/python3
import json

with open('/home/jacky/learning/json/l.json') as f:
    data=json.load(f)

a=json.dumps(data,indent=4,sort_keys=True)
print(a)

for i in range(0,4):
    print(json.dumps(data['recruitment']['job_ads'][i]['days'],indent=3,sort_keys=True))

