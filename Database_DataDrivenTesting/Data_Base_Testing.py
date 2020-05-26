#Data Driven Testing by using Database table data .
'''
from selenium import webdriver
import cx_Oracle
import time
con = cx_Oracle.connect('system/Manoj320320320')
cursor = con.cursor()
query="select * From employees"
cursor.execute(query)

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

for cols in cursor:
    driver.find_element_by_name("userName").send_keys(cols[0])
    driver.find_element_by_name("password").send_keys(cols[1])
    driver.find_element_by_name("login").click()
    time.sleep(5)
    if driver.title == "Find a Flight: Mercury Tours:":
        print ("Test is passed")
    else:
        print ("Test is failed")
    driver.find_element_by_link_text("Home").click()
'''

#if you get any errors regarding database please refer these links first .
#https://www.oracletutorial.com/tips/oracle-initialization-or-shutdown-in-progress/
#https://manjaro.site/how-to-fix-ora-00743-log-read-detects-lost-write-in-thread/
#https://asktom.oracle.com/pls/apex/asktom.search%3Ftag%3Dora-01034-oracle-not-available

'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    query="create table Manoj(ename varchar2(10),epass varchar2(10))"
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



'''
import cx_Oracle
try:
    con=cx_Oracle.connect('system/Manoj320320320')
    cursor=con.cursor()
    query = "insert into Manoj values(:ename,:epass)"
    records=[("manoj","a.manoj16"),("anki","20000"),("jyothi","30000")]
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