'''
import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
'''
from Properties_File_INI.INI_File import browser_name

'''
import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("simple.json", "w") as outfile:
    json.dump(dictionary, outfile)
'''

'''
import json

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object)) 
'''


'''
l1=[{"name":"manoj","age":29,"job":"software"},{"name":"anki","age":28,"job":"architect"}]
print (l1[0])
print (l1[0].get("name"))
print (l1[0].get("age"))
print ("**********")
print (l1[1])
print (l1[1].get("name"))
print (l1[1].get("age"))
'''


#How to create a json file in python
'''
import json

# Data to be written
l1=[{"Name":"Manoj",
     "Company":"Cisco",
     "Job":"Python tester"
     },
    {"Name":"Anki",
     "Company":"Wipro",
     "Job":"Java tester"}]

# Serializing json
json_object = json.dumps(l1, indent=4)

# Writing to sample.json
with open("simple.json", "w") as outfile:
    outfile.write(json_object)
'''

#How to read json file
'''
import json

# Opening JSON file
with open('simple.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print ("**********")
print (json_object[0])
print (json_object[0].get("Name"))
print (json_object[0].get("Company"))
print ("**********")
print (json_object[1])
print (json_object[1].get("Name"))
print (json_object[1].get("Company"))

print(type(json_object))
'''

#HOW TO MERGE TWO DICTIONARIES
'''
x={"a":10,"b":20}
y={"c":30,"d":40}
z={**x,**y}
print (z)
'''


'''
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

'''

'''
import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
'''


'''
import json
data = {}
data['browser'] = []
data['browser'].append({
    'name': 'Chrome'
})
data['browser'].append({
    'name': 'Firefox'
})
data['browser'].append({
    'name': 'Ie'
})

with open('browser.json', 'w') as outfile:
    json.dump(data, outfile)
'''



import json
from selenium import webdriver
with open('browser.json') as json_file:
    data = json.load(json_file)
    for p in data['browser']:
        browser_name=p['name']
        print(browser_name)
        
