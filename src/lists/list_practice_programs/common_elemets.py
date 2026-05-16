#find common elements b/w 2 lists

list1=[1,2,3,3,4]
list2=[1,3,5,3,4]

#using sets

common=set(list1).intersection(set(list2))
print(list(common))

#logic

common=[]
for num in list1:
    if num in list2 and num not in common:
        common.append(num)
print(common)

#