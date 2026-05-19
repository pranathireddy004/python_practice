#file handling is modifying / performing operations on files and storing

#file operations- read, write,append,delete,check for file if exist or not, loop through folder files

#file opening- 1
file=open('sample.txt','r')
c=file.read()
print(c)
file.close() #ths is must 

#best method to open a file
with open('sample.txt','r') as file:
    file_content=file.read()
    print(file_content) #here we dont need to specify file.close(()) as we are using with so it automatically closes the file



#files modes- r,w,a,x,rb,wb

#r-reads only (reads file)

#read whole file
with open('sample.txt','r') as f:
    content=f.read()
print(content)

#read line by line
with open('sample.txt','r') as f:
    for line in f:
        # print(line) #create extra spaces
        print(line.strip()) #will no craete extra gap

#read all lines as list
with open('sample.txt','r') as f:
    line=f.readlines()
    print(line) #gives \n for every lin/item in list
    f.seek(0) #bring back the pointer to zero
    lines=[line.strip() for line in f] #this wont give \n
    print(lines)

#w-writing to file

with open('temp.txt','w') as f:
    f.write('pranathi')
    f.write(' hey')

with open('temp.txt','w') as f:
    f.write('hii') #here it deletes the old data from file and add the new data

#a- append the data into file(just write deletes the old data but append adds new data)

with open('temp.txt','a') as f:
    f.write('\nPranathi')

#pathlib and path

from pathlib import Path
path=Path('sample.txt') #creates path object
print(path.exists())

with open(path,'r') as f:
    con=f.read()
    print(con)

#path has many menthods.
print(path.is_file()) #checks weather path has file
print(path.is_dir()) #checks weather path points to folder

#get content
cont=path.read_text() #similar to read
print(cont)

path.write_text('hello')

#create directirory

# folder=Path('sample.txt')
# folder.mkdir(exist_ok=True)

#delete file

# path.unlink()

#find matching files 

folder=Path('')
for file in folder.glob('*.txt'):
    print(f"file {file}")


# rglob searches inside folders

for file in folder.rglob('*txt'):
    print("1")