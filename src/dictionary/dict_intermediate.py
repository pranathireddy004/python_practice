#nested dict

employee_1={
    'id':1,
    'details':
    {
        'name':'Pranathi',
        'age':23,
        'salary':300000
    }
}

print(employee_1['details']['name'])

for key,value in employee_1.items():
    print(key,value)
    if isinstance(value,dict):
        print(f"{key} is nested dict")
        for key1,value1 in value.items():
            print(key1,value1)

# isinstance(value,datatype) return true if value is of the data type else false

#List of dicts
employees=[
    {"id":10,"name":'Pranathi',"salary":300000},
    {"age":20,"location":"Banglore"}
]
print(employees)
print(employees[0])
#loop throgh list of dicts

for emp in employees:
    if isinstance(emp,dict):
        for key,value in emp.items():
            print(key,value)

