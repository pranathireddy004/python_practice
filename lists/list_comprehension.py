#comprehension generally performing data trainsofrmation, data filtering i same line instead of uing loops

names=["M.John","H.harry","james"]
#use case: replace . with spaace in names if no . present ignore

#without comprehension
list=[]
for name in names:
    print(name)
    if '.' in name :
        name=name.replace('.',' ')
        print(name)
        list.append(name)
print(list)

#with comprehension
list1=[name. replace('.',' ') for name in names if '.' in name]
print(list1)