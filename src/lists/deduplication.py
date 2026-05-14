#deduplication is removing duplicates in a list by converting into a set

List=[1,1,2,3,4,3,5,2]
print("list with duplicates: ",List)

#convert into set

List=set(List)
print("list: ",list)

#convert back into list
List=list(List)
print("list without duplicates: ",List)