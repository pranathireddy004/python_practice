#convert csv rows to json
#we can use dictreader in csv as dict reader reads rows in dict format and we can easily convert to json
import csv
with open('employee_data.csv','r') as f:
    data=list(csv.DictReader(f))
    print(data)
import json
with open('employee_data.json','w') as f:
    json.dump(data,f,indent=2)
