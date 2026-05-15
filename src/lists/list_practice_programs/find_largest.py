#find largest element

#method 1 -using sorting

list1=[2,1,0,6,4,7,5]

list2=list1
list2.sort()
print(list2[-1])
#using max
print(max(list1))

#using logic
temp=0
for num in list1:
    if num>temp:
        temp=num

print(temp)
