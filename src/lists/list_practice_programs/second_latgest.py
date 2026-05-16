#find second largest number in list

#useing sort

list1=[1,3,5,1,6,9,12,3]

list1.sort()
print(list1[-2])

#using logic

nums=[2,1,4,7,8,10,3,9]
largest=float('-inf')
second_largest=float('inf')

for n in nums:
    if n>largest:
        second_largest=largest #if n is high then largest becomes bigger and obviosly second one will the largest variable
        largest=n
    elif n>second_largest: #if n is <largest but is >second largest obviosly until now n is second largest
        second_largest=n

print(second_largest)