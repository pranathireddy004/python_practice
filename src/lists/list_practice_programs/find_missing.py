#find missing num in range

list=[1,2,5,3]
range1=6

#method1
missing=[]
i=1
for j in range(range1):
    if i not in list:
        missing.append(i)
    i=i+1
print(missing)

#or
missing=[]
i=1
while i<=range1:
    if i not in list:
        missing.append(i)
    i=i+1
print(missing)

#method2 using list comprehension

missing=[i for i in range(1,range1+1) if i not in list]
print(missing)


#using sets
set1 = set(range(1, range1 + 1))   # {1, 2, 3, 4, 5, 6}
list1 = set(list)                  # {1, 2, 4, 6}

missing = set1.difference(list1)

print(list(missing))   







