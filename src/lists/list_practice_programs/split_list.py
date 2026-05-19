#split list into chunks

n=[1,2,3,4,5,6,7,8]
chunk_size=3
temp=[]
for i in range(0,len(n)):
    if (i+chunk_size)>len(n):
        temp1=[]
        for i in range(len(n)):
            temp1.append(n[i])
        temp.append(temp1)
    else:
        temp1=[]
        for j in range(chunk_size):
            temp1.append(n[i])
            i=i+1
        temp.append(temp1)
print(temp)

