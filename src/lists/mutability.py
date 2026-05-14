#mutablity of list
list1=[1,'two',3]
list1.append(10) #add element to the list
print(list1)
def number():
    # list1.append(4)
    a=list1+[4] #list1 does not modify as we are no using append
    return a
def alfa():
    list1.append('five') #list1 modify as we are using append 
    b=list1
    return b
print("numeric function",number())
print("alfa function",alfa())
print(list1)
