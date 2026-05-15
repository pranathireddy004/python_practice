#remove duplicates
#case 1: without preseving order

list1=[1,2,3,4,1,1,2]
list1=list(set(list1))
print(list1) #doesnt preserve order as sets are onordered

#case2: preserve order use dict

list2=[1,3,2,2,3,1,4,4,6]
list2=list(dict.fromkeys(list2))
print(list2) #preserves order as dict are orderd