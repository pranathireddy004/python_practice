#tuple is orderd collection, immutable and duplicates allowed.

data=(1,2,3)
for a in data:
    print(a)

print(data.count(1)) #used to count accourence of an item in tuple

print(len(data))

print(data.index(3)) #throws eeoor if passed arg is not in the tuple

# a[1]=2 not possivle throws error

#accessing values throgh indexing

for i in range(len(data)):
    print(data[i])
#negitive indexing

print(data[-1])

#single value tuple
a=(3,) #without , treats as integer

#most used tuple unpacking

details=("pranathi",300000)
name,salary=details
print(name,salary)

#returning multipl values from a function most used and imp

def get_data():
    return ("pranathi",30000)
name,salary=get_data()
print(name,salary)

#tuple packing

a=1,2,3
print(a)

#nested tuple

test=(1,2,(3,4))
print(test[2][0])