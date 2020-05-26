from selenium import webdriver
import time
class webtable():
    def table(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/html/html_tables.asp")
        rows=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")) #count no of rows
        columns=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))#count no of coloumns
        print ("Total no of rows are:-",(rows))
        print ("Total no of columns are:-",(columns))

        for r in range(2,rows+1):
            for c in range(1,columns+1):
                value=driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print (value,end="           ")
            print ()
w=webtable()
w.table()