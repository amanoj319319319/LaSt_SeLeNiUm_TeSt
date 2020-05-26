from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(6)

#In selenium python, we should use dictionary as a HashMap
#HashMap is nothing but key and value pair
login_info={"username":"a.manoj16@gmail.com","password":"santhuji"}

user_name=driver.find_element_by_name("email")
user_name.send_keys(login_info["username"])

pass_word=driver.find_element_by_name("pass")
pass_word.send_keys(login_info["password"])

login_button=driver.find_element_by_xpath("//*[@id='u_0_b']")
login_button.click()

driver.quit()