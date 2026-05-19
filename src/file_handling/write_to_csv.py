#writting to csv file

#writing list of lists to csv file
import csv
employees=[['name,age,dept,salary'],['pranathi','23','DE',3000000]]

with open('employee_data.csv','w',newline='') as f:
    writer=csv.writer(f) #csv.writer() is used to write rows to file and only for list of list
    writer.writerows(employees)
    writer.writerow(['john','23','DE',2500000]) #writerows to write multiple rows, writerow is to write a single row

#writing list of dicts to csv file

employee_history=[{'name':'pranathi','company':'Modak','annual_salary':600000},{'name':'Pranathi','company':'abc','annual_salary':3000000},{'name':'pranathi','company':'xyz','annual_salary':5000000}]
with open('employee_history.csv','w',newline='') as f:
    schema=['name','company','annual_salary']
    writer=csv.DictWriter(f,fieldnames=schema)
    writer.writerows(employee_history)
    writer.writerow({'name':'pranathi','company':'PMR','annual_salary':7500000})
#we can use 'a' mode to append the data
