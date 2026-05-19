#write data to json file
import json

data={
    'Pranathi':[{'company':'Modak','salary':600000},{'company':'abc','salary':3000000}]
}

with open('pranathi.json','w') as f:
    json.dump(data,f,indent=2)

#for text file if we read then it convertes to string but where as json id converts to python object that is dictionary
