'''
import configparser
config=configparser.ConfigParser()
config.add_section("Facebook_Credentials")
config.set("Facebook_Credentials", "username", "a.manoj16@gmail.com")
config.set("Facebook_Credentials", "password", "santhuji")
#config.set("Facebook_Credentials","URL","https://www.facebook.com/")

config.add_section("Facebook_Credentials_Locater_Values")
config.set("Facebook_Credentials_Locater_Values", "username_text_id", "email")
config.set("Facebook_Credentials_Locater_Values", "password_text_id", "pass")

config.add_section("Browser_Things")
config.set("Browser_Things", "Browser_name", "chrome")
config.set("Browser_Things", "URL", "https://www.facebook.com/")

with open('Facebook.ini','w') as configfile:
    config.write(configfile)
'''


import configparser
config=configparser.ConfigParser()
config.read("Facebook.ini")

user_name=config.get("Facebook_Credentials","username")
pass_word=config.get("Facebook_Credentials","password")

username_text_id=config.get("Facebook_Credentials_Locater_Values","username_text_id")
password_text_id=config.get("Facebook_Credentials_Locater_Values","password_text_id")

browser_name=config.get("Browser_Things","Browser_name")
url=config.get("Browser_Things","URL")
#print (user_name)
#print (pass_word)


'''
import configparser
#fd=open("Facebook.ini","r")
#print (fd.read())
#fd.close()

config=configparser.ConfigParser()
config.read("Facebook.ini")

user_name=config.get("Facebook_Credentials","username")
pass_word=config.get("Facebook_Credentials","password")
#print (user_name)
#print (pass_word)
'''
