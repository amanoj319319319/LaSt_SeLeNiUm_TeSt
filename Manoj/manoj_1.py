#swapping two numbers with and without using third variable
'''
def fun():
    a=10
    b=5

    #a=a+b
    #b=a-b
    #a=a-b
    #print (a,b)

    temp=a
    a=temp-b
    b=b+a
    print (a,b)
fun()
'''
'''
import os
file=[]
# List all files in a directory using os.listdir
basepath = 'C:\\Users\\Manoj\\PycharmProjects\\LastSeleniumTest\\Files\\'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(file.append(entry))
print (file)
file_name=file[0]
print (file_name)

#fd = open('C:\\Users\\Manoj\\PycharmProjects\\LastSeleniumTest\\Files\\'+f):
fd=open(basepath+file_name,"r")
a=str.splitlines(fd.read())
print (a)


'''

from Files.manoj_list import variables
v=variables()
print (v.user_name)
print (v.password)
