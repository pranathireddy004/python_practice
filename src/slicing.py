#slicing is used to fetch sub string/sublist based on indexing

x='hello'
print(x[1:3]) #start index inclusive, end index excluded

#x[start:end:step] step is how many steps to tak from one index to next, by default its 1.

print(x[0:3:2])
#reverse a struing use ::-1
print(x[::-1])

#usecase is to find a string/num is palidrome or not
x=121
if str(x)==str(x)[::-1]:
    print(f"{x} is palindrome")

#one more palindrom method
y=x
reverse=0
while x>0:
    digit=x%10
    reverse=reverse*10+digit
    x=x//10
if reverse==y:
    print(True)