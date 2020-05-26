'''
1)How to download the python from the python official website .
Official website of python is ( download python -you will find diff ver of python)

2)Once we download the python in the windows machine , we need to configure python path
in system properties . how to configure python means ,

click on computer - properties -Advanced system settings -
Environment variables - System variables - Path(here we need to give the path without ,
disturbing the existing path) - click on ok .

3)How to install selenium for python 3.x versions in windows machine .

just click on serch programs and files - enter cmd - we have to write like this -
pip install selenium .

4)How to find out the version of python in windows ?

just click on serch programs and files - enter cmd - python -V

5)If we want to check the list of the packages , just click on serch programs and files - enter cmd -,
pip list

6)IDE Options for python development
    1)Anaconda
    2)Pycharm

7)On python default IDLE ,
a="manoj"
print (a)

'''



'''
a="manoj"
print (a)

answer is --- manoj.

why did we get the value of an a is like with out quotes (manoj) means , inside of,
the print statement by default they have written quotes .Thats why we will get only ,
the values with out quotes such as single or double .False

if we want to know the information of any module or any function , we need to use ,
help() function .just you can pass the module or function inside of an paranthesis of 
help()

'''


import pdb
#pdb.set_trace()
first_name=input("Enter your first name:-")
last_name=input("Enter your last name:-")
full_name=(first_name+last_name)
print ("Full name is:-",full_name)
print ("*********************")
pdb.set_trace()
college_name=input("Enter your college name:-")
college_code=input("Enter your college code:")
combine=college_name+str(college_code)
print ("Combine is :-",combine)













