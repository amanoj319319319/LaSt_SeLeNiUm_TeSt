#connecting to the database using database credentials and finding version of the database
'''
import cx_Oracle
con=cx_Oracle.connect('system/Manoj319319319')
if con!=None:
    print ("successfully connected")
    print ("Version is:-",con.version)
else:
    print ("connection failed")
'''


#creating a table name in the database
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj319319319')
    query="create table employees(eno number,ename varchar2(10),esal number(10,2))"
    cursor=con.cursor()
    cursor.execute(query)
    print ("Table created succesfully")
except Exception as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''
#deleted a particular table name in the database
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj319319319')
    query="drop table employees"
    cursor=con.cursor()
    cursor.execute(query)
    print ("Table dropped succesfully")
except Exception as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''
#creating a table in the database
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj319319319')
    query="create table employees(eno number,ename varchar2(10),esal number(10,2))"
    cursor=con.cursor()
    cursor.execute(query)
    print ("Table created succesfully")
except Exception as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''

#Inserting multiple values to the required paramters in the employees table
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    cursor=con.cursor()
    query = "insert into employees values(:eno,:ename,:esal)"
    records=[(101,"manoj",10000),(102,"anki",20000),(103,"jyothi",30000)]
    cursor.executemany(query,records)
    con.commit()
    print ("Record Inserted succesfully")
except Exception as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

'''

#Reading input from the console
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    cursor=con.cursor()
    while True:
        eno=int(input("Enter employee number:-"))
        ename =(input("Enter employee name:-"))
        esal = float(input("Enter employee salary:-"))
        query = "insert into employees values(%d,'%s',%f)"
        cursor.execute(query %(eno,ename,esal))
        con.commit()
        print ("Records Inserted succesfully")
        option=input("Do you want to insert one more record[yes/no]")
        if option == "no":
            break
except Exception as e:
    print (e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''

#Updating records in the database using SQL query
#The employees whose salary was less than 5000,i i had to increment Rs 1000 to their existing salary
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    cursor=con.cursor()
    increment=float(input("Enter increment amount:-"))
    salaryrange=float(input("Enter salary range:-"))
    query="update employees set esal=esal+%f where esal<%f"
    cursor.execute(query %(increment, salaryrange))
    con.commit()
    print ("Records are updated successfully")

except Exception as e:
    print (e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''

#Deleting records from the employees table based on their salary ranges
#in the temployees table whose salary was greater than 5000 they were deleted from the table by me
'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    cursor=con.cursor()
    cutoff=float(input("Enter cutoff amount:-"))
    query="delete from employees where esal>%f"
    cursor.execute(query %(cutoff))
    con.commit()
    print ("Records are deleted successfully")

except Exception as e:
    print (e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
'''