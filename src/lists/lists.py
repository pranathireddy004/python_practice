#Creating a list
list=[1,2,3,'four',5,'ten','hello']
print("list =",list)

#indexing list
print("1st element of list ",list[0])

#negitive indexing
print("last element of list ",list[-1]) #usefull for processing latest record

# slicing (accessing sublist) list[startindex:stopindex]
print("last 2 elements of list ",list[5:7]) #stop index is excluded

print("first 2 elements of list ",list[:2]) #startindex will be zero

print("last 4 elemnets ",list[3:])

print(list[:-3])

#Appending list

list.append(10)
print("new list ", list)
list.append([1,2]) #appending a list 
print("new list ",list)

#extend() adds multiple items
list1=['a','b']
list1.extend([1,2])
print("new list1",list1)

#inserting insert() method inserts at particular index
data=[1,2,3]
data.insert(1,2) #insert(index,value)
print("data: ",data )

#removing elements

#remove() removes by value
data.remove(2)
print("data after removing: ",data)
#if mutiple same values are there removes one value 

#pop() removes but index
data.pop(1)
print("after poping: ",data)

#Looping throgh list
items = ["book","pen","monney"]
for item in items: #we use this more often
    print(item)

#checking the item exixts in list

print('book' in items) #return bool Value

#lenght of list
print(len(items))

#sorting
num=[3,1,5]
num.sort()
print(num)

#desc sorting
num.sort(reverse=True)
print(num)

#reverse list
num.reverse()
print(num)

# nested list
data=[[1,2],[3,4]]
print(data[0])
print(data[0][1])

for item in data:
    print(item)
    print("length: ",len(item))

#joining 2 lists
a=[1,2]
b=[3,4]
c=a+b
print("3rd list ",c)

#enumerate is used to count index and value

a=[1,2,3,4]
for index,num in enumerate(a):
    print(f"index {index}, value {num}")
    
#zip (used to combine columns or data)

name=['jhon','jack']
age=[11,12]
for n,a in zip(name,age):
    print(n,a)

#split function very important(splits a string based on delimeter)

raw_data="101,pranathi,300000"
data=raw_data.split(",") #splits based on , and converts into list
print(data)

#join reverse of split
data = ["apple", "banana", "mango"]

data_raw = ",".join(data)

print(data_raw)