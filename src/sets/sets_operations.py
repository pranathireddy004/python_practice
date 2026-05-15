#sets are unordered collection, has no duplicates, fastert than list as it has hasing implemented inside.

set_1={1,2,3}
print(set_1)

# removes duplicates
set_2={1,1,2,4,3,3}
print(set_2)

#empty set
data=set()
print(data)

data.add(1)
data.add(2)
print(data)
data.remove(2) #gives error if remove arugemnt is not present in se
data.discard(3) #no error safe to use

print(data)

#set oeprations -union,intersection,difference,symmetric diff

data_1={1,2,3}
data_2={3,4,5}

print(data_1.union(data_2)) #combiles 2 sts

print(data_1.intersection(data_2)) #only common

print(data_1.difference(data_2)) #only values present in set 1
print(data_1.symmetric_difference(data_2)) #values not common in both sets

#loop through set

for a in data:
    print(a)

nums=set([1,2,3])
print(nums)

#frozen set cant modify
temp=frozenset([1,2,3])

#set comprehension --transformation, loop and condition single line

names={'pranathi','dhanush','chimtu','pavan'}

names_1={name.upper() for name in names if len(name)>6}
print(names_1)