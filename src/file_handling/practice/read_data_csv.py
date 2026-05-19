#read data and print each line in csv
import csv

with open('sample.txt') as f:
    data=csv.reader(f)
    for line in data:
        print(line)

#count no of rows that is number of employee records excluding header
x=0
with open('sample.txt','r') as f:
    data=csv.DictReader(f)
    for row in data:
        x=x+1
print(x)

#checj if header is present or not

with open('orders.csv','r') as f:
    data=csv.reader(f)
    f.seek(0)
    temp=f.read(1024)
    temp1=csv.Sniffer().has_header(temp)
    print(temp1)

#print only employee names of csv file

with open('sample.txt','r') as f:
    data=csv.DictReader(f)
    for row in data:
        print(row['name'])

#find sum of salary
sum2=0
sum1=0
with open('sample.txt','r') as f:
    data=csv.DictReader(f)
    for row in data:
        sum2=sum2+int(row['salary'])
    #using comprehension
    f.seek(0)
    data=csv.DictReader(f)
    sum1=sum([int(row['salary']) for row in data])
print(sum2)
print(sum1)

#find max salary
with open('sample.txt','r') as f:
    data=csv.DictReader(f)
    list1=[int(row['salary']) for row in data]
    print(list1)
    max_val=max(list1)
    print(max_val)

#filter employee with salary greater that 55000

with open('sample.txt','r') as f:
    data=csv.DictReader(f)
    list=[row['name'] for row in data if int(row['salary'])>55000]
    print(list)
