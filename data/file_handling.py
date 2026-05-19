#open a file, read a file and read content of the file line by line

with open('temp.txt','r') as f:
    print(f)
    con=f.read() #is a string 
    print(isinstance(con,str))
    print(con)
    for c in con:
        print(c) #when loop like this each character will be printed
    f.seek(0)
    for line in f:
        print(line.strip())

#write
with open('sample.txt','w') as f:
    f.write('I am pranathi')
    f.write('\ni am 22 years old') 


#append
with open('sample.txt','a') as f:
    f.write('\ni earn 30lacks per annum')

#path
from pathlib import Path
path=Path('temp.txt')
print(path)
print(path.exists()) #check if file present or not

#read
print(path.read_text())
# with open(path,'r') as r:
#     con=r.read()
#     print(con)

#write text
path.write_text('hey all')
print(path.read_text())

#glob to check the pattern files
folder=Path('.')
print(folder.exists())
for f in folder.glob('*.txt'):
    print(f)