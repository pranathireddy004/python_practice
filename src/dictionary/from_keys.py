#fromkeys is  method in dict used to create keys using iterable obejcts like list

a=[1,2,3]
dict_1=dict.fromkeys(a,10) #10 is value by defualt it would be none 
print(dict_1)

#remove duplicates form list while preserving order

b=[1,2,2,2,3,1,6]
nums=dict.fromkeys(b,10)
nums=list(nums)
print(nums)