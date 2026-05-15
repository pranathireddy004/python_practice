#reverse list

list1=[1,2,3,4]

#using reverse method
list1.reverse()
print(list1)

#using slicing
reversed_list=list1[::-1]
print(reversed_list)

#using logic

reversed_list=[]

for i in range(len(list1)-1,-1,-1):
    reversed_list.append(list1[i])
print(reversed_list)

# range(start indes,stop index,step)->step decides how much to move by default 1 here we are decresing the ramge so we gave -1
