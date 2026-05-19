#csv is comma seperated values
#read csv file
# #normal method
with open('orders.csv','r') as f:
    print(f)
    con=f.read()
    print(con)
    f.seek(0)
    for line in f:
        print(line.strip().split(','))
    f.seek(0)
    list1=[line.strip().split(',') for line in f]
    print(list1)

#using csv function
import csv

#csv reader

with open('orders.csv','r') as f:
    data=csv.reader(f)
    print(data)
    for line in data:
        print(line) #we dont need to strip,split it automaticaly does and print as list for each line
    list2=[line for line in data]
    print(list2)

#read each row as dictionary

with open('orders.csv','r') as f:
    data=csv.DictReader(f) #header 1st line becomes keys and remains line becomes valuues
    for row in data: 
        print(row)
    f.seek(0)
    data=csv.DictReader(f)
    list3=[row for row in data]
    print(list3)
    
