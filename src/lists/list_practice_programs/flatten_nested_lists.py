#flatten nested lists

nums=[[1,2],[3,2,3],[1,7],10]
new=[]
for num in nums:
    if isinstance(num,list):
        for n in num:
            new.append(n)
    else:
        new.append(num)
print(new)

#using list comphrehension, nested list comprehension

# new1=[n for num in nums if isinstance(num,list) for n in num]
new1 = [
    item
    for num in nums
    for item in (num if isinstance(num, list) else [num])
]

print(new1)


# flat = [item for sublist in nested for item in sublist]
