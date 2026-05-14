#dictionary is key-value pair

employee={"name":'Pranathi',
          "age":23,
            "salary":300000}
print(f"employee: {employee}")

#its like a json

#accessing dict based on key
print("name: ",employee["name"])

#add new key-value
employee["location"]='banglore'
print(employee)

#modify existing value
employee["salary"]=350000
print(employee)

#delete key
del employee["location"]
print(employee)

#loop dict

for emp in employee:
    print(emp) #gives keys
#values
for emp in employee.values():
    print(emp)

#both key value
for key,value in employee.items():
    print(f"{key}:{value}") #items is most used

#get method
print(employee.get("name")) #safer that [] as it does not give error if key not ;present

# accessing keys, values, items
print(employee.keys())
print(employee.values())
print(employee.items())

# check if key exits
temp='salary' in employee
if 'salary' in employee:
    print("True")

if 350000 in employee.values():
    print("True")

#update method is used to add 2 dicts, add value to dict, modifying existing value

dict_1={'name':'pranathi'}
dict_2={'age':23}
dict_1.update(dict_2)
print(dict_1)

#add new values
dict_1.update({'salary':300000})
print(dict_1)
#update existing values
dict_1.update({'salary':350000})
print(dict_1)
#mix of add and update
dict_1.update({'location':'Banglore','salary':'355000'})
print(dict_1)

