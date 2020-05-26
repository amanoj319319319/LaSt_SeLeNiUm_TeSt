'''
import json

# Data to be written
l1=[{"Browser":"Chrome"
     },
    {
     "Fb_url":"https://www.facebook.com",
     "Username":"a.manoj16@gmail.com",
     "Password":"santhuji"
     },
    {
     "Letscode_url":"https://learn.letskodeit.com/p/practice",
     "Name":"Java tester"}]

# Serializing json
json_object = json.dumps(l1, indent=4)

# Writing to sample.json
with open("facebook.json", "w") as outfile:
    outfile.write(json_object)
'''

#How to read json file

import json

# Opening JSON file
with open('facebook.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print ("**********")
#print (json_object[0])
browser=(json_object[0].get("Browser"))
print ("**********")
#print (json_object[1])
fb_url=(json_object[1].get("Fb_url"))
user_name=(json_object[1].get("Username"))
pass_word=(json_object[1].get("Password"))
print ("**********")
#print (json_object[2])
lets_url=(json_object[2].get("Letscode_url"))
name=(json_object[2].get("Name"))

print(type(json_object))

