#json is similar to dict key-value pairs. Json file format is most usefull in data engineering to store configs, API responses to send the result to xcoms and manyy.

#json- javascript object notation used to store structured data

#json methods- load, dump, loads, dumps


import json

with open('pranathi.json','r') as f:
    data=json.load(f)
    print(data)
    for key,value in data.items():
        print(key,value)
    for a in data['Pranathi']:
        print(a)

#when we read a text file it converts to string but a json it converts to dict back

dict1={'data':[{'name':'pr'},{'name':'s'}]}
for a in dict1['data']:
    print(a['name'])
    for a in a['name']:
        print(a)