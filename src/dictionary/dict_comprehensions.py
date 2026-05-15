#transformation. loop and filtering in a single line

#usecase: create a new dict from employee dict, which keeps only string values and also convert them to uppercase

employee={"name":'pranathi',
          "age":23,
          "salary":"three lack per month"}

employee_new={k.upper(): v.upper() for k,v in employee.items() if isinstance(v,str)}
print(employee_new)

#complex dict

api_data={
    'status_code':200,
     'employee_response':{
         "name":"pranathi",
         "age":23,
         "job_details":[
             {"company_1":"Modak analytics",
              "salary":44000},
              {"company_1":"deloite",
               "salary":300000}
         ],
         "intrests":"Singing"
     }
}
print(api_data)

#loop over api_data

for key,value in api_data.items():
    if isinstance(value,dict):
        for key1,value1 in value.items():
            if isinstance(value1,list):
                for l in value1:
                    print(l)
            else:
                print(key1,value1)
    else:
        print(key,value)

structured_employee={
    "employee_name":api_data["employee_response"]["name"],
    "employee_age":api_data["employee_response"]["age"],
    "total_amount": sum(job_detail["salary"] for job_detail in api_data["employee_response"]["job_details"])
}

print(structured_employee)

#counting frequency of items in a list using dictionay

names=['a','a','b','c','d']
counts={}
for name in names:
    print(counts.get(name,0))
    counts[name]=counts.get(name,0)+1
    
print(counts)