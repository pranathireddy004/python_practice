#average

list1=[1,2,3,4,5]
avg=sum(list1)/len(list1)
print(avg)

#count even and odds

list2=[1,2,3,4,5,6]

even=0
odd=0
for num in list2:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)